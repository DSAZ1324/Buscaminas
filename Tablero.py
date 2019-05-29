from Casilla import Casilla


class Tablero:
    ancho = 0
    largo = 0

    def __init__(self, ancho, largo):
        self.ancho = int(ancho)
        self.largo = int(largo)

    def crear_tablero(self):
        tab = []
        casilla = []
        for x in range(self.ancho):
            for y in range(self.largo):
                if len(casilla) < self.largo:
                    casilla.append(Casilla(x, y))
            tab.append(casilla)
            casilla = []
        return tab

    def ganar(self):
        casillas_libres = 0
        casillas_reveladas = 0
        for x in range(len(Tablero.crear_tablero(self))):
            for y in range(len(Tablero.crear_tablero(self)[0])):
                if Casilla.numero(Tablero.crear_tablero(self)[x][y]) == 0:
                    casillas_libres += 1
        for x in range(len(Tablero.crear_tablero(self))):
            for y in range(len(Tablero.crear_tablero(self)[0])):
                if Casilla.numero(Tablero.crear_tablero(self)[x][y]) == 0 and Casilla.estad(
                        Tablero.crear_tablero(self)[x][y]) == True:
                    casillas_reveladas += 1
        if casillas_libres == casillas_reveladas:
            return True
        else:
            return False
