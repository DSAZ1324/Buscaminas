import random


class Casilla:

    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.estado = False
        self.num = random.randint(0, 4)
        self.valor = ''

    def posicion(self):
        return self.x, self.y

    def estado(self):
        return self.estado

    def alerta_bomba(self, opcion):
        if self.valor == '*':
            self.estado = False
        else:
            self.estado = opcion

    def numero(self):
        return self.num

    def posible_bomba(self, opcion):
        if opcion == '*':
            self.valor = '*'
        elif opcion == '?':
            self.valor = '?'
        else:
            self.valor = ''

    def obtener_bandera(self):
        return self.valor
