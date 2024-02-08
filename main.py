import requests
from flask import Flask, jsonify

app = Flask(__name__)

def get_lang_stats(repos: list) -> dict:
    try:
        langs_stats = {}

        for repo in repos:  
            language = repo['language'] or 'Unknown' 
            if language in langs_stats:
                langs_stats[language]["count"] += 1
            else:
                langs_stats[language] = {"count": 1, "percentage": 0}

        total_repos = len(repos)
        for lang in langs_stats:
            langs_stats[lang]['percentage'] = round((langs_stats[lang]['count'] / total_repos) * 100, 2) if total_repos > 0 else 0
        
        return langs_stats
    except Exception as e:
        return {
            'error_message': 'Error: Something went wrong',
            'exception_details': str(e)
        }, 500
    

@app.route('/user/<username>', methods=['GET'])
def info(username: str):
    if not username:
        return jsonify({'message': 'Error: Username is empty'}), 400
    
    try:
        response = requests.get(f'https://api.github.com/users/{username}/repos')
        
        if response.status_code != 200:
            return jsonify({'message': 'Error: User not found'}), 404
        
        repos = response.json()
        lang_stats = get_lang_stats(repos)

        if 'error_message' in lang_stats:
            return jsonify(lang_stats), lang_stats.get('status', 500)

        return jsonify(lang_stats), 200
    except requests.exceptions.RequestException as e:
        return jsonify({'message': 'Error: Something went wrong', 'exception_details': str(e)}), 500

@app.route('/<mssg>')
def hello_world(mssg):
    return jsonify({
        'message': f'{mssg}!'
    })

if __name__ == '__main__':
    app.run(debug=True)
