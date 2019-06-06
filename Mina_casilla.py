from Casilla import Casilla


class Mina(Casilla):

    def __init__(self, x, y):
        """
        crea las minas en el tablero

        :param x: int con las minas ubicadas para el eje en x
        :param y: int con las minas unicadas para el eje en y
        """
        super().__init__(x, y)
        self.num = 1
