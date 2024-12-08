###THIS IS THE ROOTIC AUDIO LIBRARY - DON"T USE IT###
import os
from gtts import gTTS

#conversion from tts
def create_tts_file(story):
    audio = gTTS(text= story, lang = 'en', slow = False)
    audio.save('bedtime_story.mp3')

#playing the audion 
def play_tts_file():
    os.system('start bedtime_story.mp3')
    
    
bedtime =open("story_text.txt","r")
bedtime_story = bedtime.read()

create_tts_file(bedtime_story)
play_tts_file()