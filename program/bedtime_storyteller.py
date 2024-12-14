import logger
import communciation_ChatGPT
import global_static_variables as gsv
import T2S_openAI

prompt = ''

# SETTING A PROMPT BASED ON USER CHOICES
def setting_a_prompt(choices):
    # generating a prompt 
    global prompt
    prompt = f"Create a bedtime story with prospect of continuation about {choices['mc']} who goes to {choices['p']} for {choices['m']} with {choices['f']} and there is a {choices['t']} twist. Write it in {gsv.current_language}"
    logger.c_print(__name__, "Setting a prompt: " + prompt)

# story_text, a file that contains the new story and all continuations
# audio_text, a file that only contains the text that gets turned into audio

def create_a_new_story():
    if prompt == '':
        raise Exception("Prompt can't be empty.")
    logger.c_print(__name__, "Creating a new story.")
    # creating a new story
    content = communciation_ChatGPT.ChatGPT_API(prompt)
    # open a txt file for storing story 
    story_text = open('resources/story_text.txt', 'w', encoding="utf-8")
    story_text.write(content)
    story_text.close()
    # open a txt file for generating audio
    audio_text = open('resources/audio_text.txt', 'w', encoding="utf-8")
    audio_text.write(content)
    audio_text.close()


def continue_the_story():
    logger.c_print(__name__, "Creating a continuation of the story.")
    # open a txt file to read it 
    story_text = open('resources/story_text.txt', 'r', encoding="utf-8")
    temp_story_text = story_text.read()
    # generating continuation of the story 
    prompt_continue = communciation_ChatGPT.ChatGPT_API("Create a continuation of the given story: \"" + temp_story_text + f"\". Write it in {gsv.current_language}")
    story_text.close()
    # open a txt file for storing story 
    story_text = open('resources/story_text.txt', 'w', encoding="utf-8")
    story_text.write(temp_story_text + "\n" + prompt_continue)
    story_text.close()
    # open a txt file for generating audio
    audio_text = open('resources/audio_text.txt', 'w', encoding="utf-8")
    audio_text.write(prompt_continue)
    audio_text.close()

def create_T2S():
    audio_text = open('resources/audio_text.txt', 'r', encoding="utf-8")
    T2S_openAI.create_audio(audio_text.read())
    audio_text.close()