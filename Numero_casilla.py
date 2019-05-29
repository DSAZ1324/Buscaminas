from Casilla import Casilla


class Numero(Casilla):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.contador = 0
        self.num = 0

    def buscar_minas(self, matriz):
        for casilla_x in range(max(self.x - 1, 0), min(self.x + 2, len(matriz))):
            for casilla_y in range(max(self.y - 1, 0), min(self.y + 2, len(matriz[0]))):
                if Casilla.numero(matriz[casilla_x][casilla_y]) == 1:
                    self.contador += 1
