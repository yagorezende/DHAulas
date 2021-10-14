# import sys
# print("Version:", sys.version)
numero = 1
texto = "12"
decimal = 12.6 # float
print("\n\n")

#### CRUD - CREATE READ UPDATE DELETE ####
## CREATE
lista = []
lista = list()
lista = [1, 2, 2, 3]
pessoas = ["Aline", "Carol", "Monica"]
print("pessoas antes", pessoas)
lista = ["Aline", 2, [1, 3]] # Nao é recomendado

pessoas.append("Raquel") # inserindo um novo elemento
pessoas.append("Raquel") # inserindo um novo elemento
print("pessoas depois", pessoas)

## READ
# as listas começam com indice 0
print("Aluna:", pessoas[2])
pos_aluna = pessoas.index("Raquel") # <- int
print("Aluna indice:", pos_aluna, pessoas[pos_aluna])
tam_lista = len(pessoas)
print("Tamanho da lista:", tam_lista)
print("Ultimo elemento:", pessoas[tam_lista-1])

## UPDATE
pessoas[tam_lista -1] = "Larissa"
print("pessoas depois", pessoas)

## DELETE
del(pessoas[-2])
print("pessoas depois", pessoas)
aluna = pessoas.pop(2)
print("pessoas depois", pessoas, "aluna removida:", aluna)

# INSERT
pessoas.insert(2, aluna)
print("pessoas depois", pessoas)

# REMOVE
pessoas.remove("Aline")
print("pessoas depois", pessoas)