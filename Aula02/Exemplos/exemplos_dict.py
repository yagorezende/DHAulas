print("\n\n")

pessoasx = {
    "pessoa1": {
        "nome": "Pedro",
        "endereco": {
            "rua": "Alfeneiros",
            "cidade": "Londres"
        }
    }
}
pessoasx["pessoa1"]["nome"] = "Marcos"
print(pessoasx["pessoa1"]["endereco"]["rua"].upper())

#### CRUD - CREATE READ UPDATE DELETE ####
# CREATE
pessoas = {} # dict vazio
pessoas = dict()
#print("Dicionario:", pessoas)

pessoas["aluna1"] = "Aline"
#print("Dicionario depois:", pessoas)

pessoas["aluna2"] = "Monica"
#print("Dicionario depois:", pessoas)

# READ
#print("Aluna 1:", pessoas["aluna1"])
#print("Aluna 1:", pessoas.get("aluna1", "essa chave nao existe"))

# UPDATE
pessoas["aluna1"] = "Larissa"
#print("Dicionario depois:", pessoas)

# DELETE
del(pessoas["aluna1"])
#print("Dicionario depois:", pessoas)

# MAIS
pessoas = {
    "aluna1": {
        "nome": "Aline",
        "idade": 23,
        "email": "aline@gmail.com"
    }
}

print("Dicionario:", pessoas)
aluna = pessoas.get("aluna1").get("nome")
idade = pessoas.get("aluna1").get("idade")
print("Aluna:", aluna, "tem", idade, "anos")

# JSON
import json

print(pessoas, type(pessoas))
# Transforma um dict em um objeto json
json_obj = json.dumps(pessoas)
print(json_obj, type(json_obj))
# Transforma um objeto json em um dict
novo_dict = json.loads(json_obj)
print(novo_dict, type(novo_dict))
aluna = novo_dict.get("aluna1").get("nome")
idade = novo_dict.get("aluna1").get("idade")
print("Aluna:", aluna, "tem", idade, "anos")