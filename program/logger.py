from datetime import datetime

def c_print(sender, text):
    print('['+datetime.now().strftime('%H:%M:%S')+']['+sender+'] '+text)