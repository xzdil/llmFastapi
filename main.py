import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from typing import AsyncGenerator
from llama_index.core import set_global_tokenizer
from transformers import AutoTokenizer
from llama_index.llms.llama_cpp import LlamaCPP
from faiss import index
from model import saiga_mistral
set_global_tokenizer(
    AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)
llms = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    llms["llama"] = saiga_mistral
    llms["query"] = index.as_query_engine(llm=llms["llama"], streaming=True, vector_store_query_mode="mmr")
    yield


app = FastAPI(lifespan=lifespan)


def run_llm(question: str) -> AsyncGenerator:
    llm: LlamaCPP = llms["llama"]
    response_iter = llm.stream_complete(question)
    for response in response_iter:
        yield response.delta


def run_query(question: str) -> AsyncGenerator:
    query_engine = llms["query"]
    for response in query_engine.query(question).response_gen:
        yield response


@app.get("/llm")
async def root(question: str) -> StreamingResponse:
    return StreamingResponse(run_llm(question), media_type="text/event-stream")


@app.get("/query")
async def root(question: str) -> StreamingResponse:
    return StreamingResponse(run_query(question), media_type="text/event-stream")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
