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
        for i in range(self.ancho):
            for j in range(self.largo):
                if len(casilla) < self.largo:
                    casilla.append(Casilla(i, j))
            tab.append(casilla)
            casilla = []
        return tab
