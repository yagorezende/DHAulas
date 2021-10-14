print("\n")
# Informações de entrada
tickets = {"OLXToday": 0.05, "OLXBlackFriday": 0.12}
cliente = {"id": 12, "nome": "Clara", "compras": 1, "ticket": "OLXBlackFriday"}
produto = {"id": 34, "nome": "Notebook Intel i9", "preco": 1789.99}

desconto = 0 # desconto em porcentagem
# Testando o desconto da primeira compra
if cliente.get("compras") == 0:
    desconto = 0.1 # (10/100) -> 10%

# Testando o desconte de ticket
ticket = cliente.get("ticket")
if ticket in tickets.keys():
    # Testando se o valor de desconto do ticket é maior que o desconto anterior
    desconto_ticket = tickets.get(ticket)
    if desconto < desconto_ticket:
        desconto = desconto_ticket

# Calculando o valor de desconto
valor_desconto = produto.get("preco") * desconto
valor_final = produto.get("preco") - valor_desconto

## [Informando o Cliente sobre os descontos]
if desconto > 0:
    print(f"Parabéns pela sua compra, {cliente.get('nome')}!")
    if cliente.get("compras") == 0 and desconto == 0.1:
        print(f"{cliente.get('nome')}, por ser sua primeira compra você recebeu um super desconto de {desconto*100}%!")
        print(f"{cliente.get('nome')}, sua compra está saindo por R$ {valor_final:.2f}")
    else:
        print(f"{ticket} ativo! Valor de desconto aplicado na compra")
        print(f"Voce recebeu um desconto de {desconto*100}% e sua compra está saindo por R${valor_final:.2f}!")
else:
    print(f"{cliente.get('nome')}, sua compra está saindo por R$ {valor_final:.2f}")