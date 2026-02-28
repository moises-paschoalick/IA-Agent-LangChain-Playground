# User → LLM → Response
# No agents

from dotenv import load_dotenv
from pprint import pprint
from providers import (
    get_openai_model
)

load_dotenv()

def test_model(model, question):
    response = model.invoke(question)
    
    print("\n=== RESPONSE ===")
    print(response.content)
    

    print("\n=== METADATA ===")
    print(response.content)

def main():
    question = "What's the capital of the Moon?"
    
    print("\n--- OpenAI ---")
    openai_model = get_openai_model(temperature=1.0)
    test_model(openai_model, question)
    
if __name__ == "__main__":
    main()    