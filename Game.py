import time
from Casilla import Casilla
from Numero_casilla import Numero
from Mina_casilla import Mina
from Tablero import Tablero


tab = []


def ganar(tab):
    casillas_libres = 0
    casillas_reveladas = 0
    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if Casilla.numero(tab[x][y]) == 0:
                casillas_libres += 1
    for x in range(len(tab)):
        for y in range(len(tab[0])):
            if Casilla.numero(tab[x][y]) == 0 and Casilla.estad(tab[x][y]) == True:
                casillas_reveladas += 1
    if casillas_libres == casillas_reveladas:
        return True
    else:
        return False
