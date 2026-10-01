from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

topic = input("Enter a topic: ")

prompt = f"""
Create 5 flashcards about {topic}.

Format each flashcard exactly like this:

Flashcard 1
Question: ...
Answer: ...

Flashcard 2
Question: ...
Answer: ...

Keep the questions simple and the answers concise.
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n" + response.choices[0].message.content)