import os 
from openai import OpenAI

#creating a client 
client = OpenAI()

# creating and saving audio
def create_audio(prompt):
    speech_file_path="bedtime_story.mp3"
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="nova",
        input=prompt,
    ) as response:
        response.stream_to_file(speech_file_path)