import pandas as pd
import numpy as np
import os
import time
from actor import Actor
from IPython.display import clear_output

# INICIALIZACIÓN
# de data frames y actores
df = pd.read_csv('actors.csv')
df.reset_index();

actors = []
federation = []
pirates = []

for _, row in df.iterrows():
    actor = Actor(row["Name"],
                  row["Faction"],
                  row["HP"],
                  row["DP"],
                  row["AP"])
    
    actors.append(actor);
    if actor.faction == "Federation":
        federation.append(actor);
    elif actor.faction == "Space Pirates":
        pirates.append(actor);

# FUNCIONES
clear = lambda: os.system('cls') # para limpiar la consola

def gameOver(federation, pirates): # para comprobar condición bucle principal
    fedsAlive = any(actor.hp > 0 for actor in federation) 
    pirsAlive = any(actor.hp > 0 for actor in pirates) 
    return fedsAlive <= 0 or pirsAlive <= 0



# INTRO
print("¡FEDERACIÓN GALÁCTIVA VS PIRATAS ESPACIALES!\n")    
print("Soldados de la Federación: ")
for soldier in federation: 
    print(soldier.name, " ", end = "")
print("\n\nPiratas espaciales: ")
for pirate in pirates: 
    print(pirate.name, " ", end = "")
print();
# time.sleep(3);



# BUCLE PRINCIPAL
clear();
print("¡El combate empieza en...!")
# time.sleep(1);
for i in range(3, 0, -1):
    print("¡", i, "!", end='', flush = True)
    # time.sleep(1)
    print('\r' + ' ' * 30, end = '', flush = True)   
    print('\r', end = '', flush = True)  
    
print("¡YA!")
# time.sleep(1);

# para debugear...
# federation[0].hp = 0
# federation[1].hp = 0
# federation[2].hp = 0

pirates[0].hp = 0
pirates[1].hp = 0
pirates[2].hp = 0

while (not gameOver(federation, pirates)):
    clear();
    print("Es el turno de" "\n")
    
    action = input("1. Atacar 2. Defender\nAcción: ");    
    
    if (action == "1"):
        time.sleep(0.01)
    elif (action == "2"):
        time.sleep(0.01);
    else:
        print("Acción inválida, inténtalo de nuevo.\n")
        time.sleep(1.5)
        continue
    
    time.sleep(0.5);
    
    
    
# FIN DEL JUEGO
clear();
print("¡FIN DEL JUEGO!\n")    
time.sleep(0.5);
time.sleep(0.5);

if any(actor.hp > 0 for actor in federation):
    for i in range(4):
        print("Ha ganado" + "." * i, end = '\r')
        time.sleep(1)
    time.sleep(1);
    print("\n¡LA FEDERACIÓN GALÁCTICA!")
else:
    for i in range(4):
        print("Han ganado" + "." * i, end = '\r')
        time.sleep(1)
    time.sleep(1);
    print("\n¡LOS PIRATAS ESPACIALES!")   
time.sleep(1);
print("¡Enhorabuena!\n Muchas gracias por jugar.")
time.sleep(1);