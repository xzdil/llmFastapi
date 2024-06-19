import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import StreamingResponse, HTMLResponse
from typing import AsyncGenerator
import gradio as gr

from llama_index.core import set_global_tokenizer
from transformers import AutoTokenizer
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core import Settings
from vectorstores.vectorstorefaiss import index, embed_model 
from models.saiga_ollama import llm
from models.gradio_api import Gradio_LLM
from db_agent2 import sql_database

from gradio_app import db_chat, doc_chat, llm_chat, main

set_global_tokenizer(
    AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)
llms = {}
Settings.embed_model = embed_model

from gradio_code import gr_code, is_local

@asynccontextmanager
async def lifespan(app: FastAPI):
    if is_local:
        llms["saiga"] = llm
    else:
        llms["saiga"] = Gradio_LLM(model_path=gr_code)
    llms["query"] = index.as_query_engine(llm=llms["saiga"],embed_model=embed_model, streaming=True, similarity_top_k=1)    
    llms["db_agent"] = NLSQLTableQueryEngine(sql_database=sql_database, tables=["rental_portfolio"],llm=llms['saiga'])   
    yield
    llms.clear()

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

app = FastAPI(lifespan=lifespan)

@app.get("/", response_class=HTMLResponse)
async def read_item():
    with open("main.html", "r") as file:
        html_content = file.read()                                                                                            
    return HTMLResponse(content=html_content)                                                                               

@app.get("/llm")
async def root(question: str) -> StreamingResponse:
    return StreamingResponse(run_llm(question), media_type="text/event-stream")

@app.get("/query")
async def root(question: str) -> StreamingResponse:
    return StreamingResponse(run_query(question), media_type="text/event-stream")

@app.get("/db_agent")
async def root(question: str):
    return run_db_agent(questiom)

app = gr.mount_gradio_app(app, db_chat, path="/db_chat")
app = gr.mount_gradio_app(app, doc_chat, path="/doc_chat")
app = gr.mount_gradio_app(app, llm_chat, path="/llm_chat")
