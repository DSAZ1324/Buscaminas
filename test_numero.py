from unittest import TestCase
from Numero_casilla import Numero
from Tablero import Tablero


class TestNumero(TestCase):
    def test_buscar_minas(self):
        ancho = 8
        largo = 8
        tablero = Tablero(ancho, largo)
        tab = tablero.crear_tablero()
        x = 3
        y = 4
        numero = Numero(x, y)
        numero.buscar_minas(tab)
        num_es = numero.contador
        self.assertEqual(num_es, numero.contador)
