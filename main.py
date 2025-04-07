users:list[dict] = [
    {'name': 'Julia', 'location': 'Płońsk', 'posts': 500, },
    {'name': 'Emilia', 'location': 'Lublin', 'posts': 400, },
    {'name': 'Martyna', 'location': 'Ząbki', 'posts': 200, }
]

for user in users:
    print(f'Twój znajomy: {user["name"]} z {user["location"]} opublikował {user["posts"]}')
