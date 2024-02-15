import requests
from flask import Flask, Response
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import os
import io


app = Flask(__name__)
plt.switch_backend('agg')


def get_lang_stats(repos: list) -> dict:
    """
    Calculate the language statistics for a list of repositories.

    Args:
        repos (list): A list of repositories.

    Returns:
        dict: A dictionary containing the language statistics, with the language name as the key and the count and percentage as the values.

    Raises:
        Exception: If something goes wrong during the calculation, an exception is raised with an error message and exception details.
    """
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


def create_chart(lang_stats: dict) -> io.StringIO:
    """
    Create a pie chart based on language statistics in SVG format.

    Args:
        lang_stats (dict): A dictionary containing language statistics.

    Returns:
        io.StringIO: A StringIO object containing the generated chart image in SVG format.
    """
    cmap = cm.get_cmap('Blues')
    norm = mcolors.Normalize(vmin=0, vmax=len(lang_stats))
    colors = cmap(norm(range(len(lang_stats))))
    
    data = [(lang, stats['percentage']) for lang, stats in lang_stats.items()]
    data_sorted = sorted(data, key=lambda x: x[1], reverse=True)
    
    labels, sizes = zip(*data_sorted)

    fig, ax = plt.subplots(figsize=(6, 4), facecolor="#20232a")
    wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=180, colors=colors)

    plt.setp(texts, fontsize=8, color='#5AA5E7', fontweight='bold')
    plt.setp(autotexts, fontsize=8, color="#20232a")

    ax.axis('equal')
    svg_buf = io.StringIO()
    plt.savefig(svg_buf, format='svg', bbox_inches='tight')
    svg_buf.seek(0)
    plt.close(fig)
    return svg_buf


@app.route('/user/<username>', methods=['GET'])
def info(username: str) -> Response:
    """
    Retrieves information about a GitHub user and generates a language statistics chart in SVG format.

    Args:
        username (str): The GitHub username.

    Returns:
        Response: The Flask Response object with the SVG image.
    """
    if not username:
        return "Error: Username is empty", 400
    
    try:
        response = requests.get(f'https://api.github.com/users/{username}/repos')
        
        if response.status_code != 200:
            return "Error: User not found", 404
        
        repos = response.json()
        lang_stats = get_lang_stats(repos)

        if 'error_message' in lang_stats:
            return lang_stats['error_message'], 500

        svg_image = create_chart(lang_stats)
        return Response(svg_image.getvalue(), mimetype='image/svg+xml')
    except requests.exceptions.RequestException as e:
        return f"Error: Something went wrong - {e}", 500


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)