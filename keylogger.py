import os 
from pynput.keyboard import Listener




with Listener(on_press=on_press) as Listerner:
    Listener.join()