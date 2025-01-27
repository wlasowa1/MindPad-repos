import time 
import logger
import RPi.GPIO as GPIO #library that works just on raspberry pi
import global_static_variables as gsv
import bedtime_storyteller
import sound_handler 

#variables for storing user choices
current_choices = {
    'mc': None,
    'p': None,
    'm': None,
    'f': None,
    't': None
}

#button callback functinons
def yes(channel):
    logger.c_print(__name__, "Button yes was pushed!")
    if gsv.state == "startup" or gsv.state == "new story":
        gsv.state = "create mc"
        logger.c_print(__name__, "Changed state to " + gsv.state)
        sound_handler.play_sound(gsv.PROMPTS[gsv.current_language]["choose_main_character"])
    elif gsv.state == "continue story":
        sound_handler.play_sound_loop(gsv.SOUNDS["intro"])
        bedtime_storyteller.continue_the_story()
        bedtime_storyteller.create_T2S()
        sound_handler.stop_sound()
        sound_handler.play_sound("resources/bedtime_story.mp3")
        sound_handler.play_sound(gsv.PROMPTS[gsv.current_language]["continue_story"])
    


def volume_up(channel):
    logger.c_print(__name__, "Button volume_up was pushed!")
    sound_handler.update_volume("up")

def volume_down(channel):
    logger.c_print(__name__, "Button volume_down was pushed!")
    sound_handler.update_volume("down")

def play_pause(channel):
    logger.c_print(__name__, "Button play_pause was pushed!")
    sound_handler.toggle_play_pause()

def no(channel):
    logger.c_print(__name__, "Button no was pushed!")
    if gsv.state == "startup" or gsv.state == "new story":
        sound_handler.play_sound(gsv.PROMPTS[gsv.current_language]["goodnight"])
        sound_handler.play_sound(gsv.SOUNDS["outro"])
        gsv.state = "startup"
        logger.c_print(__name__, "Changed state to " + gsv.state)
    elif gsv.state == "continue story":
        gsv.state = "new story"
        logger.c_print(__name__, "Changed state to " + gsv.state)
    
def language(channel):
    logger.c_print(__name__, "Button language was pushed!")
    _change_language()

def select_option_row1(channel):
    _select_option(22)

def select_option_row2(channel):
    _select_option(23)

def select_option_row3(channel):
    _select_option(24)

def _select_option(pin):
    logger.c_print(__name__, "Button in row " + str(pin) + " was pushed!")
    if gsv.state == "create mc":
        _create_choice("mc", gsv.main_character[pin], "p", "choose_place")
    elif gsv.state == "create p":
        _create_choice("p", gsv.place[pin], "m", "choose_mission")
    elif gsv.state == "create m":
        _create_choice("m", gsv.mission[pin], "f", "choose_friend")
    elif gsv.state == "create f":
        _create_choice("f",  gsv.friend[pin], "t", "choose_twist")
    elif gsv.state == "create t":
        current_choices["t"] = gsv.twist[pin]
        logger.c_print(__name__, "t was set to: " +current_choices["t"])
        gsv.state = "prompt set"
        logger.c_print(__name__, "Changed state to " + gsv.state)
        sound_handler.play_sound_loop(gsv.SOUNDS["intro"]) #playing intro music in loop
        bedtime_storyteller.setting_a_prompt(current_choices) #setting a prompt 
        bedtime_storyteller.create_a_new_story()
        bedtime_storyteller.create_T2S()
        sound_handler.stop_sound()
        sound_handler.play_sound("resources/bedtime_story.mp3")
        sound_handler.play_sound(gsv.PROMPTS[gsv.current_language]["continue_story"])
        gsv.state = "continue story"
        # START NO REACTION TIME - ADD LATER IF NEEDED! 

def _create_choice(choice_short, choice_long, new_choice_short, new_choice_long):
    current_choices[choice_short] = choice_long
    logger.c_print(__name__, choice_short + " was set to: " +current_choices[choice_short])
    gsv.state = "create " + new_choice_short
    logger.c_print(__name__, "Changed state to " + gsv.state)
    sound_handler.play_sound(gsv.PROMPTS[gsv.current_language][new_choice_long])

#function - language change
def _change_language():
    sound_handler.stop_sound()
    sound_handler.play_sound(gsv.SOUNDS["language_change"])  #play language change sound
    _reset_choices()  #reset all choices
    gsv.current_language = "polish" if gsv.current_language == "english" else "english"
    logger.c_print(__name__, "Language was changed. Current language: " + gsv.current_language)
    gsv.state = "startup"  # Restart the flowchart
    logger.c_print(__name__, "Changed state to " + gsv.state)
    sound_handler.play_sound(gsv.SOUNDS["intro"])
    sound_handler.play_sound(gsv.PROMPTS[gsv.current_language]["intro"])

#function - reset choices
def _reset_choices():
    for key in current_choices.keys():
        current_choices[key] = None
    logger.c_print(__name__, "Choices have been reset.")

#GPIO setup
logger.c_print(__name__, "Initializing of button_handler.")
GPIO.setmode(GPIO.BCM)

    #set up GPIO pins as inputs with pull-down resistors
for pin in set(gsv.main_character.keys()).union(
        gsv.place.keys(), gsv.mission.keys(), gsv.friend.keys(), gsv.twist.keys()
    ):
    logger.c_print(__name__, f"Pin {pin} has been setup with GPIO.PUD_DOWN.")
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

for pin in gsv.functional_pins.values():
    logger.c_print(__name__, f"Pin {pin} has been setup with GPIO.PUD_DOWN.")
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#setting events
logger.c_print(__name__,"Setting events")
GPIO.add_event_detect(7, GPIO.RISING, callback = yes, bouncetime=300) # 1
GPIO.add_event_detect(5, GPIO.RISING, callback = volume_up, bouncetime=300)
GPIO.add_event_detect(6, GPIO.RISING, callback = volume_down, bouncetime=300) # 7
GPIO.add_event_detect(1, GPIO.RISING, callback= play_pause, bouncetime=300)
GPIO.add_event_detect(8, GPIO.RISING, callback = no, bouncetime=300) # 8
#GPIO.add_event_detect(17, GPIO.RISING, channel = language, bouncetime=300)
GPIO.add_event_detect(22, GPIO.RISING, callback = select_option_row1, bouncetime=300)
GPIO.add_event_detect(23, GPIO.RISING, callback = select_option_row2, bouncetime=300)
GPIO.add_event_detect(24, GPIO.RISING, callback = select_option_row3, bouncetime=300)