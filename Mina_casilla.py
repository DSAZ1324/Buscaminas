from Casilla import Casilla


class Mina(Casilla):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.num = 1
