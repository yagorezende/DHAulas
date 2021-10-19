from typing import Union, List, Dict
import requests, json

def api_get(url: str)-> Union[List, Dict]:
    # result = None
    try:
        chamada = requests.get(url)
        result = chamada.status_code, json.loads(chamada.text)
    except Exception as ex:
        print("deu erro", ex)
    else:
        print("Operação bem sucedida!")
        return result
    finally:
        print("OPERAÇÃO FINALIZADA")

r = api_get("https://jsonplaceholdeRr.typicode.com/users")
# print(r)


# def exemplo_try(key, n):
#     contato = {
#         "Ana": "21 2348-5789",
#         "idade": 25
#     }
#     if contato.get(key) is not None:
#         return contato.get(key)
#     else:
#         raise Exception("Essa chave não existe no dicionario")

# # try:
# exemplo_try("telefone", 10)
# # except Exception as e:
# #     print("deu erro na chamada exemplo_try,", e)

# print("aqui!")