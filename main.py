import requests
from flask import Flask, render_template
import plotly.express as px
import os

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
        return render_template('error.html', message='Error: Username is empty'), 400
    
    try:
        response = requests.get(f'https://api.github.com/users/{username}/repos')
        
        if response.status_code != 200:
            return render_template('error.html', message='Error: User not found'), 404
        
        repos = response.json()
        lang_stats = get_lang_stats(repos)

        if 'error_message' in lang_stats:
            return render_template('error.html', message=lang_stats['error_message']), lang_stats.get('status', 500)

        # Create a Pie chart using Plotly
        fig = px.pie(lang_stats, values=[lang['count'] for lang in lang_stats.values()], names=list(lang_stats.keys()), title=f'Repo Language Distribution for {username}')
        fig.update_traces(textinfo='percent+label')
        fig.update_layout(showlegend=False)

        # Render the chart directly in the template
        chart_html = fig.to_html(full_html=False)

        return render_template('chart_template.html', chart_html=chart_html)
    except requests.exceptions.RequestException as e:
        return render_template('error.html', message='Error: Something went wrong', exception_details=str(e)), 500

@app.route('/<mssg>')
def hello_world(mssg):
    return render_template('message_template.html', message=f'{mssg}!')

@app.route('/')
def index():
    return {
        "message": "Welcome to the GitHub Stats API"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)