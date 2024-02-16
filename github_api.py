import requests

def get_user_repos(username: str) -> list:
    """
    Retrieves a list of repositories for a given GitHub user.

    Args:
        username (str): The GitHub username.

    Returns:
        list: A list of repositories.

    Raises:
        Exception: If the user is not found.
    """
    response = requests.get(f'https://api.github.com/users/{username}/repos')
    
    if response.status_code != 200:
        raise Exception("User not found")

    return response.json()