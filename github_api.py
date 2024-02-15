import requests

def get_user_repos(username: str) -> list:
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    
    if response.status_code != 200:
        raise Exception("User not found")

    return response.json()
