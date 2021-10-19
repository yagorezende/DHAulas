print("\n\n")
# 1 - criar variavel para nome
nome = "Yago Rezende"

# 2 - variavel para idade
idade = 25

# 3 - dolar hoje
dolar = 5.49

# 4 - lista mutavel de frutas
# 4.1 - forma 1
frutas = ["banana", "maçã", "goiaba", "melancia"]
#print(frutas)
# 4.2 - forma 2
frutas = [] # list()
frutas.append("banana")
frutas.append("maçã")
frutas.append("goiaba")
frutas.append("melancia")
#print(frutas)
frutas.insert(1, "limão")
#print(frutas)

# 5 - lista imutavel de caracteres
# 5.1 - forma 1
alphabeto = ("a", "b", "c")
print(alphabeto)
# 5.2 - forma 2
alphabeto = (chr(i) for i in range(97, 97+26))
print(tuple(alphabeto))
# 5.3 - forma 3 
inicio = ord("a")
fim = ord("z") + 1
alphabeto = (chr(i) for i in range(inicio, fim))
print(tuple(alphabeto))