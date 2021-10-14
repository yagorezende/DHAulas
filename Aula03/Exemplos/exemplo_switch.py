import time

# Tradução com switch/case
print("\n")
dia = "saturday"
# teste de velocidade
init_time = time.time()
match dia:
    case "monday":
        print("segunda-feira")
    case "tuesday":
        print("terça-feira")
    case "wednesday":
        print("quarta-feira")
    case "thursday":
        print("quinta-feira")
    case "friday":
        print("sexta-feira")
    case _:
        print("fim de semana!")

print(f"Switch/Case terminou em {time.time() - init_time}")

# Tradução com switch/case
# dia = "saturday"
init_time = time.time()
if dia == "monday":
    print("segunda-feira")
elif dia == "tuesday":
    print("terça-feira")
elif dia == "wednesday":
    print("quarta-feira")
elif dia == "thursday":
    print("quinta-feira")
elif dia == "friday":
    print("sexta-feira")
else:
    print("fim de semana!")
print(f"If/Else terminou em {time.time() - init_time}")


## SIMPLIFICANDO COM O OPERADOR IN
dias = ["monday", "tuesday", "wednesday", "thursday", "friday"]
dias_pt = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira"]
#dia = "tuesday"
init_time = time.time()
if dia in dias:
    print(dias_pt[dias.index(dia)])
else:
    print("fim de semana!")

print(f"If com lista terminou em {time.time() - init_time}")