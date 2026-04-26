from openai import OpenAI
import time
import sys
import random

client = OpenAI(
    api_key="APIKEY from gapgpt.app",
    base_url="https://api.gapgpt.app/v1"
)

def typePrint(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.uniform(0.025, 0.1))
    
    print()

print("Wellcome to ChatiPati, How can I assist you ? (type 'exit' to quit)\n")

while True:
    userPrompt = input("You: ")

    if userPrompt.lower() == "exit":
        print("Goodbye !")
        break

    response = client.responses.create(
        model="gapgpt-qwen-3.5",
        input= userPrompt
    )

    AIResponse = response.output_text

    print("ChatiPati: ", end="")
    typePrint(AIResponse)
