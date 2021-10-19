import requests
import json
from typing import Dict, List, Union

URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"
URL_COMMENTS = "https://jsonplaceholder.typicode.com/comments?postId="

def api_get(url: str)-> Union[List, Dict]:
    chamada = requests.get(url)
    return chamada.status_code, json.loads(chamada.text)

def busca_user(users: List, id: int) -> dict:
    for user in users:
        if user.get("id") == id:
            return user
    return None

def separa_posts(posts: List, user_id) -> List[Dict]:
    user_posts = []
    for post in posts:
        if post.get("userId") == user_id:
            user_posts.append(post)
    return user_posts