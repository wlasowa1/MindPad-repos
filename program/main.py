import logger as logger
import sound_handler
import button_handler
import global_static_variables as gsv
import time

logger.c_print(__name__, 'Starting program')
if gsv.state=="startup":
    sound_handler.play_sound(gsv.SOUNDS["intro"]) 
    sound_handler.play_sound(gsv.PROMPTS[gsv.current_language]["intro"])

while True:
    time.sleep(5)
    logger.c_print(__name__, '')