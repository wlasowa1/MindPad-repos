# -- This py file is used for handling communication with ChatGPT -- 
import os 
import logger
from openai import OpenAI 

# getting OPENAI API KEY from environment variable 
os.environ["OPENAI_API_KEY"] = "HERE_INSERT_APIKEY"

# Create client
client = OpenAI()

# Create a prompt to communication with OpenAI
def ChatGPT_API(prompt):
    logger.c_print(__name__, "Sending prompt to ChatGPT API.")
    response = client.chat.completions.create(
    model="gpt-4o",
    messages = [
        {"role": "system",
        "content": "You tell engaging bedtime stories in simple, age-appropriate language for 5-year-olds, with prospect of continuation."}, 
        {"role": "user",
        "content": prompt}
        ],
    )
    return response.choices[0].message.content
