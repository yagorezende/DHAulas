from typing import Union, List, Dict
from meus_modulos.constantes import PI

def area_circulo(raio: int | float) -> float:
    """
    Essa função calcula a área de um círculo
    :param raio: raio do círculo que se deseja calcular
    :return: valor da área de um círculo
    :rtype: float
    """
    return PI * (raio**2)

def area_triangulo(base, altura):
    return (base * altura) / 2

def multiply(a, b):
    a = a * a
    b = b * b
    c = a * b
    return a, b, c

