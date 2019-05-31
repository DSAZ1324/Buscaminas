from Casilla import Casilla


class Tablero:
    ancho = 0
    largo = 0

    def __init__(self, ancho, largo):
        self.ancho = int(ancho)
        self.largo = int(largo)

    def crear_tablero(self):
        tab = []
        for x in range(self.ancho):
            casilla = []
            for y in range(self.largo):
                    casilla.append(Casilla(x, y))
            tab.append(casilla)
        return tab
