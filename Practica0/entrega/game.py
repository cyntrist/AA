import pandas as pd
import numpy as np
import os

clear = lambda: os.system('cls')
import time
from IPython.display import clear_output

turno = False; # 0 -> J1, 1 -> J2
while (True):
    clear();
    print("Es el turno del jugador " + str(turno + 1))
    s = input();
    turno = not turno;
    time.sleep(0.5);