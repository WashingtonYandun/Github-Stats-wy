import os
from flask import Flask, Response
from github_api import get_user_repos
from stats_calculator import calculate_language_stats
from chart_generator import generate_language_stacked_bar


app = Flask(__name__)


@app.route('/user/<username>', methods=['GET'])
def info(username: str) -> Response:
    """
    Retrieves the language statistics for a given GitHub user's repositories and generates a stacked bar chart.

    Args:
        username (str): The GitHub username.

    Returns:
        Response: The stacked bar chart image in SVG format.

    Raises:
        Exception: If an error occurs during the process.
    """
    try:
        repos = get_user_repos(username)
        lang_stats = calculate_language_stats(repos)

        if 'error_message' in lang_stats:
            return lang_stats['error_message'], 500

        svg_image = generate_language_stacked_bar(username=username, lang_stats=lang_stats)
        return Response(svg_image, mimetype='image/svg+xml')

    except Exception as e:
        return f"Error: Something went wrong - {e}", 500
    

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
