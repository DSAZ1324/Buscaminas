from unittest import TestCase
from Mina_casilla import Mina


class TestMina(TestCase):
    def test___init__(self):
        x = 3
        y = 4

        num_es = 1
        mi_mina = Mina(x, y)
        self.assertEqual(mi_mina.num, num_es)
