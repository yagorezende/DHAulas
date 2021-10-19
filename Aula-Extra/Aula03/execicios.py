print("\n\n")
# 1 - par impar
"""
n = eval(input("Digite um numero para testar: "))
if int(n) % 2 == 0:
    print(f"{n} é par!")
else:
    print(f'{n} é impar!')
"""
# 2 - operação em conta
"""
saldo = 100
saque = eval(input("Digite o valor de saque: "))
if saque <= saldo:
    saldo -= saque
else:
    print("Saque negado devido ao valor contido na conta")
print(f"Valor atual da conta = R${saldo:.2f}")
"""
# 3 - 
saldo = 100
operacao = input("Digite a operação desejada (S/D): ")
if operacao.lower() == "s":
    saque = eval(input("Digite o valor de saque: "))
    if saque <= saldo:
        saldo -= saque
    else:
        print("Saque negado devido ao valor contido na conta")
elif operacao.lower() == "d":
    deposito = eval(input("Digite o valor de deposito: "))
    saldo += deposito
else:
    print("Operação inexistente!")
print(f"Valor atual da conta = R${saldo:.2f}")