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
        "content": "You tell engaging bedtime stories in simple, age-appropriate language for 5-year-olds."}, 
        {"role": "user",
        "content": prompt}
        ],
    )
    #max_tokens = 650 # Limit the response to 650 tokens
    return response.choices[0].message.content

print(ChatGPT_API("Create a bedtime story with turtle as a main character"))