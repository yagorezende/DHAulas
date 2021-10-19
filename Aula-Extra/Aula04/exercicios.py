print("\n\n")

contatos = [
    {"nome": "João", "email": "joao@gmail.com", "telefone": "(21) 91234-5678"},
    {"nome": "Maria", "email": "maria@gmail.com", "telefone": "(21) 96548-3487"},
    {"nome": "josé", "email": "jose@gmail.com", "telefone": "(21) 97865-4567"},
]

for i, contato in enumerate(contatos):# -> dict[str, str]
    print(f"-   contato:", i)
    print(f"    -   nome: {contato.get('nome')}")
    print(f"    -   email: {contato.get('email')}")
    print(f"    -   telefone: {contato.get('telefone')}")

print("\n range\n")
for i in range(len(contatos)):# : i <- int
    contato = contatos[i]
    print(f"-   contato:", i)
    print(f"    -   nome: {contato.get('nome')}")
    print(f"    -   email: {contato.get('email')}")
    print(f"    -   telefone: {contato.get('telefone')}")


print("\n while \n")
n = len(contatos)
i = 0
while i < n:
    contato = contatos[i]
    print(f"-   contato:", i)
    print(f"    -   nome: {contato.get('nome')}")
    print(f"    -   email: {contato.get('email')}")
    print(f"    -   telefone: {contato.get('telefone')}")
    i += 1