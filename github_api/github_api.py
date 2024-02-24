import requests

github_constants = {
    'base_url': 'https://api.github.com',
    'user_repos': '/users/{username}/repos',
    'user_info': '/users/{username}',
    'user_events': '/users/{username}/events',
}

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
    try:
        response = requests.get(github_constants['base_url'] + github_constants['user_repos'].format(username=username))
        
        if response.status_code != 200:
            raise Exception("User not found")
        
        if len(response.json()) == 0:
            raise Exception("User has no repositories")

        return response.json()
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with get_user_repos - {e}")


def get_user_info(username: str) -> dict:
    """
    Retrieves information about a given GitHub user.

    Args:
        username (str): The GitHub username.

    Returns:
        dict: Information about the user.

    Raises:
        Exception: If the user is not found.
    """
    response = requests.get(f'https://api.github.com/users/{username}')
    
    if response.status_code != 200:
        raise Exception("User not found")

    return response.json()


def get_user_events(username: str) -> list:
    """
    Retrieves a list of events for a given GitHub user.

    Args:
        username (str): The GitHub username.

    Returns:
        list: A list of events.

    Raises:
        Exception: If the user is not found.
    """
    response = requests.get(f'https://api.github.com/users/{username}/events')
    
    if response.status_code != 200:
        raise Exception("User not found")

    return response.json()