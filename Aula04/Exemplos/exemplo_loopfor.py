"""
ligacoes = {
    "Carla": "1234-5678",
    "Aline": "3245-6548",
    "Bianca": "6578-4654"
}

for contato, numero in ligacoes.items():
    print(f"Ligação para {contato} no número: {numero}")

nomes = list(ligacoes.keys())
numeros = list(ligacoes.values())

contatos = [{"nome": nomes[i], "numero": numeros[i]} for i in range(3)]
print(contatos)

# break
for i in range(1, 10):
    print(i, end=" ")
    if i > 5:
        break
print()

i = 1
while i <= 6:
    print(i, end=" ")
    i += 1
print()
"""

## 
frutas = ["Banana", "Maça", "Abacaxi"]
for fruta in frutas: # REPITA!
    print(fruta)

print("\n")

ligacoes = {
    "Carla": "1234-5678",
    "Aline": "3245-6548",
    "Bianca": "6578-4654"
}
# ["Carla", "Aline", "Bianca"]
# ["1234-5678", "3245-6548", "6578-4654"]
for contato, numero in ligacoes.items():
    print(f"Você recebeu de ligação {contato} do número {numero}")


print("\n")
"""
nomes = ["Carla", "Aline", "Bianca"]
numeros = ["1234-5678", "3245-6548", "6578-4654"]
for i in range(len(nomes)):
    print(f"Você recebeu de ligação {nomes[i]} do número {numeros[i]}")
"""
nomes = ["Carla", "Aline", "Bianca"]
# ["Carla", "Aline", "Bianca"] -> pop(0) -> ["Aline", "Bianca"]
# ["Aline", "Bianca"] -> pop(1) -> ["Aline"]
# ["Aline"] -> pop(2) -->> ERROR
"""for i in range(len(nomes)):
    nome = nomes.pop(i)
    print(f"Você recebeu de ligação {nome}")
""" 

print("\n\n *******")
for i in range(1, 10):
    print(i)
    if i > 5:
        break

print("\n\n * WHILE")
i = 1
while not (i > 6) and i < 10:
    print(i)
    i += 1

print("\n\n * WHILE TRUE")
i = 1
procurando = True
while procurando:
    print(i)
    if i > 5:
        procurando = False
    i += 1

print("\n\n * CONTINUE")
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

print("\n\n * CONTINUE 1")
for i in range(1, 10):
    if i % 2 != 0:
        print(i)

print("\n\n * CONTINUE 2")
for i in range(1, 10):
    if i % 2 == 0:
        pass
    else:
        print(i)

print("\n\n * FOR COM INDEX")
frutas = ["Banana", "Maça", "Abacaxi"]
# [0, 1, 2]
for indece in range(len(frutas)): # REPITA!
    print(f" * {indece} - {frutas[indece]}")

