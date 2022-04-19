import unittest
from src.logica.Conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    def test_conjunto_vacio_retornaNone(self):
        conjunto = Conjunto([])
        self.assertIsNone(conjunto.promedio())

    def test_conjunto_vacio_retornaNone(_self_):
        conjunto = Conjunto([5])
        _self_.assertIsNone(5,conjunto.promedio())
