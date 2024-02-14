import requests
from flask import Flask, send_file
import matplotlib.pyplot as plt
import matplotlib
import os
import io

app = Flask(__name__)
matplotlib.use('Agg')


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
    

def create_chart(lang_stats, username: str, chart_type: str):
    data = [(lang, stats['percentage']) for lang, stats in lang_stats.items()]
    data_sorted = sorted(data, key=lambda x: x[1], reverse=True)
    labels, sizes = zip(*data_sorted)

    fig, ax = plt.subplots()
    if chart_type == 'donut':
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig.gca().add_artist(centre_circle)

    elif chart_type == 'pie':
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    
    plt.setp(texts, size=8, weight="bold")
    plt.setp(autotexts, size=8, color="white", weight="bold")
    
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f'Repo Language Distribution for {username}', pad=20, weight='bold', size=12)

    # Save the plot to a bytes object with high DPI for better quality
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=500)
    buf.seek(0)
    plt.close(fig)
    return buf


@app.route('/user/<username>/<chart_type>', methods=['GET'])
def info(username: str, chart_type: str):
    if not username:
        return "Error: Username is empty", 400
    if chart_type not in ['pie', 'donut']:
        return "Error: Invalid chart type", 400
    
    try:
        response = requests.get(f'https://api.github.com/users/{username}/repos')
        
        if response.status_code != 200:
            return "Error: User not found", 404
        
        repos = response.json()
        lang_stats = get_lang_stats(repos)

        if 'error_message' in lang_stats:
            return "Error: Something went wrong", lang_stats.get('status', 500)

        # Create a chart based on the specified type
        image = create_chart(lang_stats, username, chart_type)
        
        return send_file(image, mimetype='image/png')
    except requests.exceptions.RequestException as e:
        return "Error: Something went wrong", 500


@app.route('/')
def index():
    return {
        "message": "Welcome to the GitHub Stats API"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)