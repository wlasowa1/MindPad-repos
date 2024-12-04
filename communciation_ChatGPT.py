import os 
from openai import OpenAI 

# getting OPENAI API KEY
os.environ.get("OPENAI_API_KEY")

# Create client
client = OpenAI()

# Create a prompt to communication with OpenAI
def ChatGPT_API(prompt):
    response = client.chat.completions.create(
    model="gpt-4o",
    messages = [
        {"role": "system",
        "content": "You are a bedtime storyteller that tells captivating bedtime stories with language suitable for 5 year old kids."}, 
        {"role": "user",
        "content": prompt}
        ],
    )
    return response.choices[0].message.content