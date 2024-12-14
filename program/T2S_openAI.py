import logger
from openai import OpenAI

#creating a client 
client = OpenAI()

# creating and saving audio
def create_audio(content):
    logger.c_print(__name__, "Creating T2S")
    speech_file_path="resources/bedtime_story.mp3"
    with client.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="nova",
        input=content,) as response:
        response.stream_to_file(speech_file_path)
    logger.c_print(__name__, "T2S created")
