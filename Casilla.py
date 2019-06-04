import random


class Casilla:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.estado = False
        self.num = random.randint(0, 4)
        self.valor = ''

    def numero(self):
        return self.num

    def estado(self):
        return self.estado

    def cambiar_estado(self, estado):
        if self.valor == '*':
            self.estado = False
        else:
            self.estado = estado

    def posible_bomba(self, opcion):
        if opcion == '*':
            self.valor = '*'
        elif opcion == '?':
            self.valor = '?'
        else:
            self.valor = ''

    def opcion(self):
        return self.valor
