print("\n\n")
nota = 8
if nota < 5: # True ou False
    print("Você está abaixo da média!")
elif nota == 6:
    print("Você está na média")
elif nota < 8:
    print("Você está acima da média!")
else:
    print("Você está muito acima da média!")

## Pontos importantes
print("\n********")
bebeu_cerveja = True # type(?)
n = ""
if not bebeu_cerveja:
    print("Pode dirigir")
else:
    # evitando divisão por zero
    if n:
        print(f"Não pode dirigir {1/len(n)}")
    else:
        print(f"Não pode dirigir 1")

print("\n")
username = "yago"
senha = "12345"
db = {"user": "yago", "senha": "123456"}
if username == db.get("user") and senha == db.get("senha"):
    print("Usuário autenticado")
else:
    print("O nome não bate")