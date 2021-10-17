from desafio_funcoes import *

URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"
URL_COMMENTS = "https://jsonplaceholder.typicode.com/comments?postId="

status, users = api_get(URL_USERS)
print(f"Há {len(users)} usuários registrados na base.")
user_id = eval(input("Digite o id do usuário a ser buscado: "))

if busca_user(users, user_id) is not None:
    status, posts = api_get(URL_POSTS)
    for post in separa_posts(posts, user_id):
        # Imprimindo o Post
        print(f" - Post: {post.get('id')}")
        print(f"   - Titulo: {post.get('title')}")
        print(f"     - Corpo: {post.get('body')}")
        # Imprimindo os comentários do Post
        status, comments = api_get(URL_COMMENTS + str(post.get('id')))
        for comment in comments:
            print(f"     - Comentário: {comment.get('id')} de {comment.get('email')}:")
            print(f"        - {comment.get('body')}")
else:
    print("ID inválido!")

