import random


class Casilla:

    x = 0
    y = 0

    def __init__(self, x, y):
        """
        Funcion para crear una casilla

        :param x: int que representa la posicion en x
        :param y: int que representa la posicion en y
        """
        self.x = int(x)
        self.y = int(y)
        self.estado = False
        self.num = random.randint(0, 4)
        self.valor = ''

    def numero(self):
        """
        el numero de la casilla
        :return: el estado del numero en la casilla
        """
        return self.num

    def estado(self):
        """
        estado actual de la casilla

        :return:el estado en que se encuentra la casilla
        """

        return self.estado

    def cambiar_estado(self, estado):
        """
        Funcion que nos permite el cambio de estado de la casilla

        :param estado: bool con el estado actual de la casilla
        :return: el cambio de estado de la casilla
        """
        if self.valor == '*':
            self.estado = False
        else:
            self.estado = estado

    def posible_bomba(self, opcion):
        """
        Funcion que permite validar identificar si se tiene una posible bomba cerca

        :param opcion: str con posibilidades para validar si hay bombas
        :return: la posible opcion que se tiene para marcar la bomba
        """
        if opcion == '*':
            self.valor = '*'
        elif opcion == '?':
            self.valor = '?'
        else:
            self.valor = ''

    def opcion(self):
        """
        permite validar la opciones dentro de una casilla

        :return: la opcion de la casilla
        """

        return self.valor
