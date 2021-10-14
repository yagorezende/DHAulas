API_URL = "https://reqres.in/api/users/2"
print("\n\n")
# API Reference
import requests
import json

call = requests.get(API_URL)
print(call.content, type(call.content))

print()
# convertendo a resposta do servidor para um dict
data = json.loads(call.content)
print(data.get("data") , type(data))
p_nome = data.get("data").get("first_name")
ult_nome = data.get("data").get("last_name")
email = data.get("data").get("email")

print()
# Imprimindo com string formatada
full_name = p_nome + " " + ult_nome
print(full_name, "tem o email:", email)
print(f"{p_nome} {ult_nome} tem o email: {email}")

## POST
