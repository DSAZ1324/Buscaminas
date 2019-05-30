from unittest import TestCase
from Tablero import Tablero


class TestTablero(TestCase):
    def test_crear_tablero(self):
        tablero = Tablero(8, 8)
        tab = tablero.crear_tablero()
        tablero_es = tab
        self.assertEqual(tab, tablero_es)

    def test_ganar(self):
        tablero = Tablero(8, 8)
        espero = False
        resultado = tablero.ganar()
        self.assertEqual(espero, resultado)
