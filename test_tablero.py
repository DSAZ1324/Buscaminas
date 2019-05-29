from unittest import TestCase
from Tablero import Tablero


class TestTablero(TestCase):
    def test_crear_tablero(self):
        ancho = 8
        largo = 8
        tablero = Tablero(ancho, largo)
        tab = tablero.crear_tablero()
        tablero_es = tab
        self.assertEqual(tab, tablero_es)
