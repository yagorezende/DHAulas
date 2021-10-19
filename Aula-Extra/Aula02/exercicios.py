print("\n\n")
# 1 - adicionando nomes na lista
nomes = []
nomes.append("João")
nomes.append("Pedro")
nomes.append("Maria")
nomes.append("Marta")
print(nomes)

# 2 - print vogais
alphabeto = (chr(i) for i in range(ord("a"), ord("z")+1))
alphabeto = tuple(alphabeto)
print("Indices das vogais:", alphabeto.index("a"),
alphabeto.index("e"),
alphabeto.index("i"),
alphabeto.index("o"),
alphabeto.index("u"))

# 3 - dicionario de nomes
nome_dict = {
    "nome": "João",
    "idade": 74,
    "telefone": "(21) 91234-5678"
}
print(nome_dict)
nome_dict["nome"] = "Marcos"
print(nome_dict)