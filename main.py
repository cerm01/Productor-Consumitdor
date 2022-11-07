from traceback import print_tb
import keyboard
import threading
import time
import random
import os


def productor(contenedor, p_productor, counter):
    while True:
        os.system('cls')
        if contenedor[p_productor] != "🍔":
            contenedor[p_productor] = "🍔"
            counter -= 1
        else:
            break
        if p_productor == 24:
            p_productor = 0
        else:
            p_productor += 1
        imprimir(contenedor, p_productor, counter, 1)
        time.sleep(1)
        if counter == 0:
            break
    return p_productor


def consumidor(contenedor, p_consumidor, counter):
    while True:
        os.system('cls')
        if contenedor[p_consumidor] == "🍔":
            contenedor[p_consumidor] = "🍽️"
            counter -= 1
        else:
            break
        if p_consumidor == 24:
            p_consumidor = 0
        else:
            p_consumidor += 1
        imprimir(contenedor, p_consumidor, counter, 2)
        time.sleep(1)
        if counter == 0:
            break
    return p_consumidor


def imprimir(contenedor, posicion, counter, bandera):
    if bandera == 1:
        print("Productor trabajando")
        print("Posicion productor: ", posicion)
        print("Restante: ", counter)
    
    if bandera == 2:
        print("Consumidor trabajando")
        print("Posicion consumidor: ", posicion)
        print("Restante: ", counter)

    for i in range(25):
        print(contenedor[i], " ", end=" ")
    print("\n")


def main():
    
    contenedor = list()
    for i in range(25):
        contenedor.append("🍽️")
    p_productor = 0
    p_consumidor = 0

    while True:

        turno = random.randint(0,100)
        counter = random.randint(2,5)

        if turno % 2 == 0:
            p_productor = productor(contenedor, p_productor, counter)

        if turno % 2 != 0:
            p_consumidor = consumidor(contenedor, p_consumidor, counter)
        
        if keyboard.is_pressed('esc'):
            break


if __name__ == '__main__':
    main()