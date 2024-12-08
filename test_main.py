import pytest
from validador import validor


def test_validor_entrada_valida():
    assert validor("a1b") == True
    assert validor("Olam5n") == True


def test_validor_inicio_invalido():
    assert validor("1ola") == False
    assert validor("0laM") == False


def test_validor_sem_numero():
    assert validor("abc") == False
    assert validor("o_o") == False


def test_validor_invalidar_tamanho():
    assert validor("olamundonovo7a") == False
    assert validor("") == False