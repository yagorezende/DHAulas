import requests
import json

from requests.api import get, post
print("\n\n")
URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"
URL_COMMENTS = "https://jsonplaceholder.typicode.com/comments?postId="

get_users = requests.get(URL_USERS)
users = json.loads(get_users.text)
print(f"Há {len(users)} usuários registrados na base.")

user_id = eval(input("Digite o id do usuário a ser buscado: "))

encontrado = False
for user in users:
    if user.get("id") == user_id:
        encontrado = True
        break

if encontrado:
    get_posts = requests.get(URL_POSTS)
    posts = json.loads(get_posts.text)
    for post in posts:
        if post.get("userId") == user_id:
            print(f" - Post: {post.get('id')}")
            print(f"   - Titulo: {post.get('title')}")
            print(f"     - Corpo: {post.get('body')}")
            
            # pegando comentários
            get_comments = requests.get(URL_COMMENTS + str(post.get('id')))
            comments = json.loads(get_comments.text)
            for comment in comments:
                print(f"     - Comentário: {comment.get('id')} de {comment.get('email')}:")
                print(f"        - {comment.get('body')}")
else:
    print("ID inválido!")