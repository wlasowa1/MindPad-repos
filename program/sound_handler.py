import time
import logger
import pygame  #library for audio play
import global_static_variables as gsv


volume_level = 0.5
is_playing = False

#initialize pygame mixer for audio play
def init():
    logger.c_print(__name__, "Initializing of sound_handler.")
    pygame.mixer.init()
    pygame.mixer.music.set_volume(volume_level)

#function - play MP3 files (thread secure function :) 
def play_sound(file_path):
    logger.c_print(__name__, f"Playing sound - {file_path}.")
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)
    logger.c_print(__name__, f"Done playing - {file_path}.")

#function - play MP3 files in loop
def play_sound_loop(file_path):
    logger.c_print(__name__, f"Playing sound loop - {file_path}.")
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops = 57)
    logger.c_print(__name__, f"Done playing sound loop - {file_path}.")

#function - stop MP3 files
def stop_sound():
    logger.c_print(__name__, "Stopping playing sound.")
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

#function to update volume level
def update_volume(direction):
    global volume_level
    if direction == "up" and volume_level < 1:
        volume_level += 0.2
        pygame.mixer.music.set_volume(volume_level)
        logger.c_print(__name__, f"volume increased to {volume_level}")
        play_sound(gsv.SOUNDS["volume_up"])
    elif direction == "down" and volume_level > 0.21:
        volume_level -= 0.2
        pygame.mixer.music.set_volume(volume_level)
        logger.c_print(__name__, f"volume decreased to {volume_level}")
        play_sound(gsv.SOUNDS["volume_down"])
    else:
        logger.c_print(__name__, "Volume remains unchanged.")

#function for play/pause
def toggle_play_pause():
    global is_playing
    if is_playing:
        logger.c_print(__name__, "Pausing...")
        pygame.mixer.pause()
        is_playing = False
    else:
        logger.c_print(__name__, "Resuming...")
        pygame.mixer.unpause()
        is_playing = True