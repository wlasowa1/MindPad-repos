import logger
import RPi.GPIO as GPIO #library that works just on raspberry pi
import bedtime_storyteller
import T2S_openAI
import button_handler
import sound_handler
import global_static_variables as gsv

init = False

if init==False:
    logger.c_print(__name__, "Initialization of system.")
    sound_handler.init()
    button_handler.init()
    init=True

if gsv.state=="startup":
    sound_handler.play_sound(gsv.SOUNDS["intro"]) 
    sound_handler.play_sound(gsv.PROMPTS[gsv.current_language]["intro"])
