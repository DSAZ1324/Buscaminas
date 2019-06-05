from Casilla import Casilla


class Numero(Casilla):

    def __init__(self, x, y):
        """
        permite ubicar los numeros en las casillas

        :param x: int con las numeros ubicados en las coordenadas de x
        :param y: int con os numeros ubicados en las coordenadas de y
        """
        super().__init__(x, y)
        self.contador = 0
        self.num = 0

    def buscar_minas(self, tablero):
        """
        Funcion que nos permite realizar a busqueda de las minas

        :param tablero: list con el tablero asignado
        :return: str con los movimiento realizados para encontrar la mina
        """
        for casilla_x in range(max(self.x - 1, 0), min(self.x + 2, len(tablero))):
            for casilla_y in range(max(self.y - 1, 0), min(self.y + 2, len(tablero[0]))):
                if Casilla.numero(tablero[casilla_x][casilla_y]) == 1:
                    self.contador += 1
        return self.contador
