import os
import time
import pygame  #library for audio play
import RPi.GPIO as GPIO
from english_bedtime_storyteller import create_a_new_story, setting_a_prompt
from T2S_openAI import create_audio

#initialize pygame mixer for audio play
pygame.mixer.init()

#function - play MP3 files
def play_sound(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

#file paths for sounds
SOUNDS = {
    "intro_english": "sounds/intro_english.mp3",
    "intro_polish": "sounds/intro_polish.mp3",
    "outro": "sounds/outro.mp3",
    "volume_up": "sounds/volume_up.mp3",
    "volume_down": "sounds/volume_down.mp3",
    "language_change": "sounds/language_change.mp3"
}

#GPIO setup
GPIO.setmode(GPIO.BCM)

#default options (easily changeable for customization)
main_character = {22: "a dog", 23: "a duck", 24: "a turtle"}
place = {22: "jungle", 23: "castle", 24: "space"}
mission = {22: "finding treasure", 23: "helping friend", 24: "adventure"}
friend = {22: "cat", 23: "owl", 24: "giraffe"}
twist = {22: "magic", 23: "special talent", 24: "surprise"}

#language-specific sentences
PROMPTS = {
    "english": {
        "intro": "It's almost bedtime, do you want to create your bedtime story?",
        "goodnight": "Goodnight!",
        "choose_main_character": "Choose your main character: {options}",
        "choose_place": "Where should the story take place: {options}",
        "choose_mission": "What should the mission of this story be: {options}",
        "choose_friend": "Who is the friend of the main character: {options}",
        "choose_twist": "What about a twist to your story: {options}"
    },
    "polish": {
        "intro": "Juz prawie czas spać, czy chcesz stworzyć twoją własną bajkę dobranockę?",
        "goodnight": "Dobranoc!",
        "choose_main_character": "Kim jest główny bohater?: {options}",
        "choose_place": "Gdzie dzieje sie historia?: {options}",
        "choose_mission": "Jaka bedzie misja tej dobranocki?: {options}",
        "choose_friend": "Kto jest przyjacielem głównego bohatera?: {options}",
        "choose_twist": "Jaki zwrot akcji dodasz do twojej bajki?: {options}"
    }
}

functional_pins = {
    'yes': 1,
    'play/pause': 7,
    'no': 8,
    'volume_down': 6,
    'volume_up': 5,
    'language': 17
}

#set up GPIO pins as inputs with pull-down resistors
for pin in set(main_character.keys()).union(
    place.keys(), mission.keys(), friend.keys(), twist.keys()
):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for pin in functional_pins.values():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#variables for storing user choices
choices = {
    'mc': None,
    'p': None,
    'm': None,
    'f': None,
    't': None
}

state = "waiting"
volume_level = 3
is_playing = False
current_language = "english"  #default language

#function to update volume level
def update_volume(direction):
    global volume_level
    if direction == "up" and volume_level < 5:
        volume_level += 1
        print(f"volume increased to {volume_level}")
        play_sound(SOUNDS["volume_up"])
    elif direction == "down" and volume_level > 1:
        volume_level -= 1
        print(f"volume decreased to {volume_level}")
        play_sound(SOUNDS["volume_down"])
    else:
        print("Volume remains unchanged.")

#function for play/pause
def toggle_play_pause():
    global is_playing
    if is_playing:
        print("Pausing story...")
        is_playing = False
    else:
        print("Resuming story...")
        is_playing = True

#function - language change
def change_language():
    global current_language, state
    play_sound(SOUNDS["language_change"])  #play language change sound
    reset_choices()  #reset all choices
    current_language = "polish" if current_language == "english" else "english"
    state = "waiting"  # Restart the flowchart
    print(f"Language changed to {current_language.capitalize()}.")

#function - reset choices
def reset_choices():
    for key in choices.keys():
        choices[key] = None

#function - dynamically format prompts
def format_prompt(options_dict):
    return ", ".join(options_dict.values())

#main program loop
try:
    while True:
        if state == "waiting":
            play_sound(SOUNDS[f"intro_{current_language}"])
            print(PROMPTS[current_language]["intro"])
            if GPIO.input(functional_pins['yes']) == GPIO.HIGH:
                time.sleep(0.5)  # Debounce
                state = "creating_story"
            elif GPIO.input(functional_pins['no']) == GPIO.HIGH:
                time.sleep(0.5)  # Debounce
                print(PROMPTS[current_language]["goodnight"])
                play_sound(SOUNDS["outro"])
                break

        elif state == "creating_story":
            for step, (prompt_key, options_dict) in zip(
                choices.keys(),
                [
                    ("choose_main_character", main_character),
                    ("choose_place", place),
                    ("choose_mission", mission),
                    ("choose_friend", friend),
                    ("choose_twist", twist),
                ],
            ):
                prompt = PROMPTS[current_language][prompt_key].format(
                    options=format_prompt(options_dict)
                )
                print(prompt)
                choice = None
                while not choice:
                    for pin, option in options_dict.items():
                        if GPIO.input(pin) == GPIO.HIGH:
                            time.sleep(0.5)
                            choice = option
                            break
                choices[step] = choice
                print(f"{step} chosen: {choice}")

            state = "playing_story"

        elif state == "playing_story":
            print("Story playing...")
            setting_a_prompt()  #use selected choices to set the prompt
            create_a_new_story()  #generate a story
            create_audio("story_text.txt")  #generate audio file
            print(PROMPTS[current_language]["goodnight"])
            reset_choices()
            play_sound(SOUNDS["outro"])
            state = "waiting"

        #volume control:
        elif GPIO.input(functional_pins['volume_up']) == GPIO.HIGH:
            time.sleep(0.5)
            update_volume("up")
        elif GPIO.input(functional_pins['volume_down']) == GPIO.HIGH:
            time.sleep(0.5)
            update_volume("down")

        #language change:
        elif GPIO.input(functional_pins['language']) == GPIO.HIGH:
            start_time = time.time()
            while GPIO.input(functional_pins['language']) == GPIO.HIGH:
                if time.time() - start_time >= 5:  # 5-second press
                    change_language()
                    break

finally:
    GPIO.cleanup()
