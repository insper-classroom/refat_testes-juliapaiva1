import pytest
from classes.Carrinho import Carrinho
import numpy as np

def test_carrinho():
    carrinho = Carrinho()
    return carrinho.adicionar_item('sabonete', 7)
