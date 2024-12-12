import os
from openai import OpenAI
from communciation_ChatGPT import ChatGPT_API
from T2S_openAI import create_audio

prompt = ""  #initialize the prompt as a global variable

# SETTING A PROMPT BASED ON USER CHOICES
def setting_a_prompt(choices):
    # Extract user choices
    selected_mc = choices['mc']
    selected_p = choices['p']
    selected_m = choices['m']
    selected_f = choices['f']
    selected_t = choices['t']

    #generate prompt dynamically
    global prompt
    prompt = (
        f"Create a bedtime story about {selected_mc} who goes to {selected_p} for {selected_m} "
        f"with {selected_f} and there is a {selected_t} twist."
    )

#create a new story
def create_a_new_story():
    # Clear existing story file
    bedtime_story = open('story_text.txt', 'w')
    bedtime_story.write('')
    bedtime_story.close()

    #generate story using ChatGPT
    content = ChatGPT_API(prompt)

    #write story content to file
    bedtime_story = open('story_text.txt', 'w', encoding="utf-8")
    bedtime_story.write(content)
    bedtime_story.close()

#continue the story
def continue_the_story():
    #clear existing story file
    bedtime_story = open('story_text.txt', 'w')
    bedtime_story.write('')
    bedtime_story.close()

    #generate continuation of a story
    continuation_prompt = "Create a continuation of the given story."
    prompt_continue = ChatGPT_API(continuation_prompt)

    #write continuation to file
    bedtime_story = open('story_text.txt', 'w', encoding="utf-8")
    bedtime_story.write(prompt_continue)
    bedtime_story.close()

#main
if __name__ == "__main__":
    # This dictionary should come from the button handling code
    choices = {
        'mc': 'a dog',
        'p': 'jungle',
        'm': 'finding treasure',
        'f': 'cat',
        't': 'magic'
    }

    #generate prompt and create a new story
    setting_a_prompt(choices)
    create_a_new_story()

    #read and convert the story to audio
    with open('story_text.txt', 'r', encoding='utf-8') as bedtime_audio:
        create_audio(bedtime_audio.read())
