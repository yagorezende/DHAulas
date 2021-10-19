# lista de usuários em que cada usuário é representado por um dict
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 4, "name": "Sue"},
    {"id": 5, "name": "Chi"},
    {"id": 6, "name": "Thor"},
    {"id": 7, "name": "Clive"},
    {"id": 8, "name": "Hicks"},
    {"id": 9, "name": "Kate"},
]

def get_user(users, id) -> dict:
    for user in users:
        if user.get("id") == id:
            return user

# lista de tuplas no qual cada par de IDs representa uma amizade
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)] 
relations = [[] for i in range(len(friendship_pairs))]
print(relations)
for persona_index, friend_id in friendship_pairs:
    persona_nome = get_user(users, persona_index)
    friend_name = get_user(users, friend_id)
    if persona_nome is not None and friend_name is not None:
        print(f"{persona_nome.get('name')} é amig@ de {friend_name.get('name')}")
    relations[persona_index].append(friend_id)

print(relations)