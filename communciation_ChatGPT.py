# -- This py file is used for handling communication with ChatGPT -- #

#importing libraries
import os 
from openai import OpenAI 

# getting OPENAI API KEY from environment variable 
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
    return response.choices[0].message.content