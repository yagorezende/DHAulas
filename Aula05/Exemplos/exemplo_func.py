from meus_modulos.funcoes import area_circulo
from typing import List
#import requests

area = area_circulo(2)

def soma(x, y):
    c = x + y
    return c

def incremento(lista: List):
    nova_lista = []
    for i in range(len(lista)):
        nova_lista.append(lista[i] + 1)
    return nova_lista

a = 3
b = 2
print(a, b)
a = soma(a, b)
print(a, b)

minha_lista = [1, 2, 3, 4]
print(minha_lista)
minha_lista = incremento(minha_lista)
print(minha_lista)

print("\n\n")
def multiply(a, b):
    a = a * a
    b = b * b
    c = a * b
    return a, b, c

a, b, c = multiply(a,b)
print(a, b, c)


def separa_nome(nome):
    nomes = nome.split()
    return nomes[0], nomes[-1]

print("***")
nome, sobrenome = separa_nome("Yago Rezende")
print(f"nome={nome}, sobrenome={sobrenome}")

def minha_funcao(param1, param2=""):
    print(param1, param2)

minha_funcao("Casa")

def minha_funcao(param1, *args, **kwargs):
    print(type(args), type(kwargs))

z = 1
def minha_funcao(z, param1, *args, **kwargs):
    z += param1
    return z, param1

z, param = minha_funcao(z, 2)
print(z)

area_retangulo = lambda lado_a, lado_b: lado_a * lado_b

print(area_retangulo(10, 10))

def area_retangulo2(func, lado_a, lado_b):
    return func(lado_a, lado_b)

print(area_retangulo2(area_retangulo, 10, 10))

"""



from meus_modulos.funcoes import *
area = area_circulo(3)
print(area)

"""