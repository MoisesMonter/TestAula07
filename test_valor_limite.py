import pytest
from validador import validor 


def test_validor_abaixo_esperado():
    assert validor("") == False
    assert validor('') == False

def test_validor_minimo_Esperado():
    assert validor("o") == True
    assert validor("1") == False

def test_validor_maximo_Esperado():
    assert validor("Ol4mund") == True
    assert validor("Olamund") == False
    
def test_validor_acima_esperado():
    assert validor("ol4mund0") == True
    assert validor("ol4munaaaad0") == True

def test_validor_tamanho_esperado():
    assert validor("O_0_la") == False
    assert validor("olao1l") == True