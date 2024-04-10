import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
import gradio as gr

from llama_index.core import set_global_tokenizer
from transformers import AutoTokenizer
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core import Settings

from vectorstores.vectorstorefaiss import index, embed_model 
from models.saiga_ollama import llm
from db_agent2 import sql_database

set_global_tokenizer(
    AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)
llms = {}
Settings.embed_model = embed_model

@asynccontextmanager
async def lifespan(app: FastAPI):
    llms["saiga"] = llm
    llms["query"] = index.as_query_engine(llm=llms["saiga"],embed_model=embed_model, streaming=True, similarity_top_k=1)
    llms["db_gent"] = NLSQLTableQueryEngine(sql_database=sql_database, llm=llms['saiga'])
    yield
    llms.clear()


app = FastAPI(lifespan=lifespan)


def run_llm(question: str) -> AsyncGenerator:
    llm = llms["saiga"]
    response_iter = llm.stream_complete(question)
    for response in response_iter:
        yield response.delta


def run_query(question: str) -> AsyncGenerator:
    query_engine = llms["query"]
    for response in query_engine.query(question).response_gen:
        yield response

def run_db_agent(question: str):
    agent = llms["db_agent"]
    return agent.query(question)


@app.get("/llm")
async def root(question: str) -> StreamingResponse:
    return StreamingResponse(run_llm(question), media_type="text/event-stream")

@app.get("/query")
async def root(question: str) -> StreamingResponse:
    return StreamingResponse(run_query(question), media_type="text/event-stream")

@app.get("/db_agent")
async def root(question: str):
    return run_db_agent(questiom)

from gradio_app import db_chat, doc_chat, llm_chat, main

app = gr.mount_gradio_app(app, db_chat, path="/db_chat")
app = gr.mount_gradio_app(app, doc_chat, path="/doc_chat")
app = gr.mount_gradio_app(app, llm_chat, path="/llm_chat")
app = gr.mount_gradio_app(app, main, path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
