import time

print("\n\n")

contador = 0
inicio = time.time() # tempo em segundos
# Enquanto a condição for verdadeira -> Repita!
while contador < 5: # condição de parada
    contador += 1
print(f"Loop acabou com {contador} repetições")

bebi_agua = input("Bebi água hoje? (S/N) ")
while bebi_agua.lower() != 's':
    bebi_agua = input("E aí? Já bebeu água hoje? (S/N) ")

print("Parabéns, agora beba mais um pouco de água")