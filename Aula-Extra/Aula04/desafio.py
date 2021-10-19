import requests
import json

from requests.api import post

API_GET_USERS = "https://jsonplaceholder.typicode.com/users"
API_GET_POSTS = "https://jsonplaceholder.typicode.com/posts"
API_GET_COMMENTS = "https://jsonplaceholder.typicode.com/comments?postId="

print("\n\n")
call = requests.get(API_GET_USERS)

# contando quanto usuários tem no sistema
usuarios = json.loads(call.text) # -> List[dict]
## print(usuarios, type(usuarios), len(usuarios))
quantidade = len(usuarios)
print(f"Há {quantidade} usuários registrados na base.")

# buscar posts de um usuário
user_id = eval(input("Digite o do usuário a ser buscado: "))

# algoritmo de busca em lista, para saber se o usuário existe ou não
encontrado = False
for user in usuarios:
    if user_id == user.get('id'):
        encontrado = True
        break

if encontrado:
    # buscando todos os posts na base
    call = requests.get(API_GET_POSTS)
    posts = json.loads(call.text) # -> List[dict]
    for post in posts: # post <- dict
        if post.get('userId') == user_id:
            print(f" - Post: {post.get('id')}")
            print(f"   - Titulo: {post.get('title')}")
            print(f"     - Corpo: {post.get('body')}")
            ## Parte II
            call = requests.get(API_GET_COMMENTS + str(post.get('id')))
            comments = json.loads(call.text) # -> List[dict]
            for comment in comments:
                print(f"       - Comentário: {comment.get('id')} de {comment.get('email')}")
                print(f"         - {comment.get('body')}")
else:
    print("Usuário inexistente na base!")
