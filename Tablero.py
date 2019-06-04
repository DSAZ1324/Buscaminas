from Casilla import Casilla


class Tablero:
    ancho = 0
    largo = 0

    def __init__(self, ancho, largo):
        """
        crea el tablero con un tamaño indicado

        :param ancho: int la anchura del tablero
        :param largo: int la altura del tablero
        """
        self.ancho = int(ancho)
        self.largo = int(largo)

    def crear_tablero(self):
        """
        nos permite crear un tablero aleatorio

        :return: el tablero creado
        """
        tab = []
        for x in range(self.ancho):
            casilla = []
            for y in range(self.largo):
                    casilla.append(Casilla(x, y))
            tab.append(casilla)
        return tab
