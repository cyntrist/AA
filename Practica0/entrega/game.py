import pandas as pd
import numpy as np
import os
import time
from actor import Actor
from IPython.display import clear_output
from enum import Enum


# INICIALIZACIÓN
# de data frames y actores
df = pd.read_csv('actors.csv')
df.reset_index();

class Factions(Enum):
    FEDERATION = "Federation"
    PIRATES = "Space Pirates"
federation = []
pirates = []

for _, row in df.iterrows():
    actor = Actor(row["Name"],
                  row["Faction"],
                  row["HP"], # Health Points
                  row["DP"], # Defense Points
                  row["AP"]) # Attack Points
    
    if actor.faction == "Federation":
        federation.append(actor);
    elif actor.faction == "Space Pirates":
        pirates.append(actor);

actors = federation + pirates # importante, según he entendido no es redundante: no duplica memoria y son referencias

# FUNCIONES
clear = lambda: os.system('cls') # para limpiar la consola

def gameOver(federation, pirates): # para comprobar condición bucle principal
    fedsAlive = any(actor.hp > 0 for actor in federation) 
    pirsAlive = any(actor.hp > 0 for actor in pirates) 
    return fedsAlive <= 0 or pirsAlive <= 0

def changeTurn(turno, j1):
    if ((turno % (len(actors)/2)) == 0): # asumimos que ambos equipos tienen la misma cantidad de pjs
        print(f"¡Turno de {'la Federación!' if j1 else 'los Piratas!'}")
        return not j1;
    return j1;

def attack(equipo, actor):
    attacked = False
    while(not attacked):
        clear();
        print("\nElige objetivo: ")
        print(" ".join([f"{i+1}. {actor.name}" for i, actor in enumerate(equipo) if actor.hp > 0]))
        try:
            objective = int(input("Objetivo: "))
        except ValueError:
            print("Acción inválida, vuelve a intentarlo.")
            continue
        if objective <= 0 or objective > len(equipo) or equipo[objective - 1].hp <= 0:
            print("Acción inválida, vuelve a intentarlo.")
            time.sleep(0.5)
            continue
        
        objective -= 1;
        victim = equipo[objective]
        if actor.ap >= victim.dp: # si consigue atravesar su escudo ataca
            victim.hp -= actor.ap;
            print("¡" + actor.name + " hirió a ", victim.name, " por ", actor.ap, " HP!")
            if victim.hp <= 0:
                print(victim.name + " ha caído en combate...")
        else:
            print("Los ataques de " + actor.name + " rebotan contra " + victim.name + ".")
            damage = int(actor.ap/2)
            victim.dp -= damage
            time.sleep(0.5)
            print("El escudo de " + victim.name + " merma en", damage, "DP.")
        attacked = True;   
        time.sleep(2);  
    
    

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
# pirates[0].hp = 0
# pirates[1].hp = 0
# pirates[2].hp = 0


turno = 0;
j1 = True;
while (not gameOver(federation, pirates)):
    clear();
    print("TURNO:", turno);
    actor = actors[turno % len(actors)]
    j1 = changeTurn(turno, j1);
    while (actor.hp <= 0):
        turno +=1
        actor = actors[turno % len(actors)]
        j1 = changeTurn(turno, j1);
    
    print("Es el turno de", actor.name)
    print("HP: ", actor.hp ," DP: ", actor.dp ," AP: ", actor.ap, "\n")
    action = input("1. Atacar 2. Esperar\nAcción: ");    
    
    if (action == "1"): # atacar
        attack(federation if actor.faction == "Space Pirates" else pirates, actor)
    elif (action == "2"): # esperar
        recovery = int(actor.hp/3);
        if recovery < 1:
            recovery = 1;
        actor.hp += recovery;
        print(actor.name, "espera y regenera", recovery, "HP.");
        time.sleep(1);
    else:
        print("Acción inválida, inténtalo de nuevo.\n")
        time.sleep(0.5)
        continue
    
    turno += 1
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