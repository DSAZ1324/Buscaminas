from unittest import TestCase
from Casilla import Casilla


class TestCasilla(TestCase):
    def test_numero(self):
        mi_casilla = Casilla(3, 4)
        espero = mi_casilla.num
        resultado = mi_casilla.numero()
        self.assertEqual(espero, resultado)

    def test_alerta_bomba(self):
        mi_casilla = Casilla(3, 4)
        mi_casilla.valor = '*'
        mi_casilla.alerta_bomba(True)
        espero = False
        resultado = mi_casilla.estado
        self.assertEqual(espero, resultado)

        mi_casilla = Casilla(3, 4)
        mi_casilla.valor = ''
        mi_casilla.alerta_bomba(True)
        espero = True
        resultado = mi_casilla.estado
        self.assertEqual(espero, resultado)

    def test_posible_bomba(self):
        mi_casilla = Casilla(3, 4)
        mi_casilla.posible_bomba('*')
        espero = '*'
        resultado = mi_casilla.valor
        self.assertEqual(espero, resultado)

        mi_casilla = Casilla(3, 4)
        mi_casilla.posible_bomba('?')
        espero = '?'
        resultado = mi_casilla.valor
        self.assertEqual(espero, resultado)

        mi_casilla = Casilla(3, 4)
        mi_casilla.posible_bomba('!')
        espero = ''
        resultado = mi_casilla.valor
        self.assertEqual(espero, resultado)
