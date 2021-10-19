from typing import Union
import requests
import json
from requests import api

from requests.api import post

API_GET_USERS = "https://jsonplaceholder.typicode.com/users"
API_GET_POSTS = "https://jsonplaceholder.typicode.com/posts"
API_GET_COMMENTS = "https://jsonplaceholder.typicode.com/comments?postId="


def api_get(url: str) -> Union[dict, list]:
    call = requests.get(url)
    return json.loads(call.text)

def busca_user(users: list, id: int) -> dict:
    for user in usuarios:
        if user_id == user.get('id'):
            return user
    return dict()

# Como melhor o desempenho dessa função?
def separa_posts(posts: list, user_id: int):
    #user_posts = []
    for post in posts:
        if post.get('userId') == user_id:
            # user_posts.append(post)
            yield post        
    #yield user_posts


print("\n\n")
# contando quanto usuários tem no sistema
usuarios = api_get(API_GET_USERS) # -> List[dict]
## print(usuarios, type(usuarios), len(usuarios))
quantidade = len(usuarios)
print(f"Há {quantidade} usuários registrados na base.")

# buscar posts de um usuário
user_id = eval(input("Digite o do usuário a ser buscado: "))

# algoritmo de busca em lista, para saber se o usuário existe ou não
encontrado = busca_user(usuarios, user_id)

if len(encontrado):
    # buscando todos os posts na base
    todos_posts = api_get(API_GET_POSTS) # -> List[dict]
    user_posts = separa_posts(todos_posts, user_id)
    print(user_posts, type(user_posts))
    for post in user_posts: # post <- dict
        print(f" - Post: {post.get('id')}")
        print(f"   - Titulo: {post.get('title')}")
        print(f"     - Corpo: {post.get('body')}")
        ## Parte II
        comments = api_get(API_GET_COMMENTS + str(post.get('id'))) # -> List[dict]
        for comment in comments:
            print(f"       - Comentário: {comment.get('id')} de {comment.get('email')}")
            print(f"         - {comment.get('body')}")
else:
    print("Usuário inexistente na base!")
