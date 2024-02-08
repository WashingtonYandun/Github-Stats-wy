import requests
from flask import Flask

app = Flask(__name__)


username = ''
api_url = f'https://api.github.com/users/{username}/repos'


@app.route('/')
def index():
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception if the response status code is not 200

        repos = response.json()
        
        name_lang = {}
        lang = []
        
        for i in range(len(repos)):
            name_lang[repos[i]['name']] = repos[i]['language']
            lang.append(repos[i]['language'])

        return {
            'repos': name_lang,
            'languages': list(set(lang)),
            'total_repos': len(repos),
            'ex': repos[0]
        }

    
    except requests.exceptions.RequestException as e:

        return {
            'message': 'Error: ' + str(e)
        }


if __name__ == '__main__':
    app.run(debug=True)