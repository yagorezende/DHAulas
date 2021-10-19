import requests
import json

API_POST = "https://reqres.in/api/register"
API_PUT_DELETE = "https://reqres.in/api/users/"

user = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}

## Parte I -> POST
call = requests.post(API_POST, data=user)
print(call, call.text, call.status_code, type(call.text))
data = json.loads(call.text)
print(data)


## Parte II -> DELETE
id = 4
call = requests.delete(API_PUT_DELETE + str(id))
print(call, call.text, call.status_code, type(call.text))

## Parte III -> PUT
id = 4
atualizacao = {
    "name": "Yago",
    "job": "UFFiano"
}
call = requests.put(API_PUT_DELETE, data=atualizacao)
print(call, call.text, call.status_code, type(call.text))