from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage

from fastapi.middleware.cors import CORSMiddleware

import json
import asyncio

load_dotenv()

app = FastAPI(title="LangChain Agent Streaming API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para dev apenas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/agent/stream")
async def agent_stream():
    """
    Endpoint streaming de um agent LangChain.
    Envia tokens para o front-end usando Server-Sent Events (SSE).
    """
    
    agent = create_agent("gpt-5-nano")
    
    # Generator async que envia tokens
    async def event_generator():
        ## Com o astream, não espera o resultado ficar pronto para enviar
        async for token, metadata in agent.astream(
            {"messages": [HumanMessage(content="Escreva sobre Luna City, a capital da Lua")]},
            stream_mode="messages"
        ):
            if token.content:
                # SSE requer prefixo 'data:'
                yield f"data: {json.dumps({'content': token.content})}\n\n"
                await asyncio.sleep(0)  # cede controle ao loop de evento

        # Indica que terminou
        yield "event: end\ndata: [DONE]\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")

