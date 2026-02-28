<h1 align="center">
  <img 
    src="https://raw.githubusercontent.com/moises-paschoalick/assets/main/logos/langchain.png" 
    width="65" 
    style="vertical-align: middle;"
  />
  <span style="position: relative; top: 3px;">
    AI Agent LangChain Playground
  </span>
</h1>


Este projeto é um **playground de IA usando LangChain** com Python, um ambiente isolado e experimental utilizado para testar:

- Uso de modelos de chat simples (`model.invoke`)  
- Criação de agentes com `create_agent`
- Conversas **multi-turn** (manutenção de contexto)
- Streaming de respostas para o frontend via **SSE (Server-Sent Events)**
- Diferença entre execução síncrona e assíncrona

## Anotações e Aprendizados
Durante a construção deste playground, os principais aprendizados foram:

- **Diferença entre chamada direta e agent**
  - `model.invoke` realiza apenas uma chamada simples ao modelo.
  - `create_agent` adiciona uma camada de orquestração, permitindo raciocínio estruturado e manutenção de contexto.

- **Multi-turn conversation**
  O contexto não é mantido automaticamente.  
  Para preservar a continuidade da conversa, é necessário reenviar todo o histórico (`HumanMessage` e `AIMessage`) a cada chamada.

- **Streaming de respostas**
  - `stream()` → execução síncrona.
  - `astream()` → execução assíncrona, ideal para integração com FastAPI.
  - O uso de **SSE (Server-Sent Events)** permite enviar tokens progressivamente ao frontend.

- **Renderização no frontend**
  - Recebimento de chunks em tempo real via `EventSource`.
  - Uso de `requestAnimationFrame` para animação mais fluida e sincronizada com o ciclo de renderização do navegador.

- **Arquitetura**
  Separação clara entre:
  - Backend simples (LLM direto)
  - Backend com agents
  - Camada de streaming
  - Frontend minimalista para visualização

Este projeto reforça conceitos fundamentais de integração entre LLMs, agents, APIs assíncronas e streaming em tempo real.

## Estrutura do projeto

- **app.py**  
  Implementação simples sem agent.  
  Fluxo: `User → LLM → Response`  
  Utiliza `model.invoke`, sem controle explícito de histórico.

- **agent_app.py**  
  Implementação utilizando agents.  
  Fluxo: `User → Agent → LLM → Response`  
  Permite conversas multi-turn enviando o histórico completo de mensagens a cada chamada.

- **agent_stream_api.py**  
  Responsável pelo streaming via SSE.  
  - `stream()` → síncrono  
  - `astream()` → assíncrono (ideal para FastAPI)  
  Permite envio progressivo de tokens para o frontend em tempo real.

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

4. Endpoint streaming: http://localhost:8000/agent/stream

Pode ser consumido via EventSource no front-end ou curl -N
```
curl -N http://localhost:8000/agent/stream
```

## Frontend

O frontend foi desenvolvido de forma simples, utilizando HTML, CSS e JavaScript puro, sem frameworks.

A comunicação com o backend ocorre via Server-Sent Events (SSE) (text/event-stream).
O cliente abre uma conexão com EventSource, recebe os tokens gerados pelo agent em tempo real e renderiza o conteúdo progressivamente na interface.

A animação de digitação utiliza requestAnimationFrame, garantindo uma atualização mais suave e sincronizada com o ciclo de renderização do navegador.
