'''Comment schematics from Better Comments extension'''
# comment
# * comment
# ! comment
# ? comment
# TODO: comment
''''''''''''''''''''''''''''''''''''''''''''''''
# THIS IS THE MAIN FILE FOR ENABLING ALL THE FUNCTIONS 

import os 
from openai import OpenAI
from communciation_ChatGPT import ChatGPT_API
from T2S_openAI import create_audio

# this is hard coded - please change this in button code, variables should be set to ''
main_character = 'dog'
place = 'castle'
mission = 'helping friend'
additional_character = 'giraffe'
twist = 'suprise'

prompt = ''

def create_a_new_story():
   
    # clear already existing file
    bedtime_story = open('story_text.txt', 'w')
    bedtime_story.write('')
    bedtime_story.close()

    # creating a new story
    content = ChatGPT_API(prompt)

    # open a txt file to write it 
    bedtime_story = open('story_text.txt', 'w', encoding="utf-8")
    bedtime_story.write(content)


def continue_the_story():
    # clearing the txt file
    bedtime_story = open('story_text.txt', 'w')
    bedtime_story.write('')
    bedtime_story.close()
    # generating continuation of the story 
    prompt_continue = ChatGPT_API('Create a continuation of the given story.')
    bedtime_story = open('story_text.txt', 'w')
    bedtime_story.write(prompt_continue)


# SETTING A PROMPT BASED ON USER CHOICES
def setting_a_prompt():
    # generating a prompt 
    global prompt
    prompt = f"Create a bedtime story about {main_character} who goes to {place} for {mission} with {additional_character} and there is a {twist} twist."


setting_a_prompt()
create_a_new_story()

bedtime_audio = open('story_text.txt', 'r', encoding='utf-8')
create_audio(bedtime_audio.read())