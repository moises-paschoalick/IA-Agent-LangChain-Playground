from langchain.chat_models import init_chat_model

def get_openai_model(temperature=0.0):
    return init_chat_model(
        model="gpt-5-nano",
        temperature=temperature
    )
    