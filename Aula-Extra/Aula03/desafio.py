import requests
import json
from datetime import date

print("\n\n")
API_LOGIN = "https://reqres.in/api/login"
API_REGISTER = "https://reqres.in/api/register"
DIAS_SEMANA = ("segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo")

user = {
    "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}

call = requests.post(API_LOGIN, data=user)
print(call.text, call.status_code, type(call.text))
if call.status_code == 200:
    token = json.loads(call.text) # -> dict {"token": valor}
    print(f"Login realizado para {user.get('email')}, recebendo o token {token.get('token')}")

    fazer_registro = input("Deseja registrar a conta logada? (S/N) ")
    if fazer_registro.lower() == "s":
        call = requests.post(API_REGISTER, data=user)
        if call.status_code == 200:
            data_registro = json.loads(call.text) # -> dict {"id": int, "token": str}
            indice_dia = date.today().weekday()
            dia_da_semana = DIAS_SEMANA[indice_dia]
            print("Registro realizado com sucesso!")
            print(f"ID: {data_registro.get('id')}, token: {data_registro.get('token')}, dia: {dia_da_semana}")
        else:
            print("Falha ao registrar conta!")
    else:
        print("não fazer registro")
else:
    print("Nome de usuário e senha incorretos")