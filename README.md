# IA-Agent-LangChain-Playground

Este projeto é um **playground de IA usando LangChain** com Python, permitindo:

- Uso de modelos de chat simples (`model.invoke`)  
- Criação de agentes (`create_agent`) com suporte a multi-turn  
- Streaming de respostas para front-end via **SSE**  

## Anotações (aprendizado)
- astream() é assíncrono; stream() é síncrono.

## Estrutura do projeto

```
langchain-playground/
│
├── app.py # Chamadas simples sem agent
├── agent_app.py # Chamadas agent sync/multi-turn
├── agent_stream_api.py # Streaming via REST API
├── providers.py # Criação de modelos e agents
├── .env-example # Exemplo de variáveis de ambiente
├── .gitignore
└── requirements.txt
```

## Pré-requisitos

- Python >= 3.10
- pip  
- API Keys para OpenAI, Anthropic e Google Gemini

## Setup do projeto

1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/IA-Agent-LangChain-Playground.git
cd IA-Agent-LangChain-Playground
```

2. Criar ambiente virtual e ativar

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

3. Instalar dependências

```bash
pip install -r requirements.txt
```

4. Configurar variáveis de ambiente

```bash
cp .env-example .env
# Editar .env e colocar suas chaves de API
```

## Executar exemplos

1. Chamadas simples com app.py
```bash
python app.py
```
2. Multi-turn agent com agent_app.py

```bash
python agent_app.py
```

3. Streaming agent via REST API (agent_stream_api.py)
```
uvicorn agent_stream_api:app --reload --port 8000
```

4. Endpoint streaming: http://localhost:8000/agent/astream

# Pode ser consumido via EventSource no front-end ou curl -N
```
curl -N http://localhost:8000/agent/astream
```

