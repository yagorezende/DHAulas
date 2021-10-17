import requests
import json
from typing import Dict, List, Union

URL_USERS = "https://jsonplaceholder.typicode.com/users"
URL_POSTS = "https://jsonplaceholder.typicode.com/posts"
URL_COMMENTS = "https://jsonplaceholder.typicode.com/comments?postId="

def api_get(url: str)-> Union[List, Dict]:
    pass

def busca_user(users: List, id: int) -> dict:
    pass

def separa_posts(posts: List, user_id) -> List[Dict]:
    pass