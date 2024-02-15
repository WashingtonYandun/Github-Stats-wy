import os
from flask import Flask, Response
from github_api import get_user_repos
from stats_calculator import calculate_language_stats
import matplotlib.pyplot as plt
from chart_generator import generate_chart

app = Flask(__name__)
plt.switch_backend('agg')


@app.route('/user/<username>', methods=['GET'])
def info(username: str) -> Response:
    try:
        repos = get_user_repos(username)
        lang_stats = calculate_language_stats(repos)

        if 'error_message' in lang_stats:
            return lang_stats['error_message'], 500

        svg_image = generate_chart(lang_stats)
        return Response(svg_image.getvalue(), mimetype='image/svg+xml')

    except Exception as e:
        return f"Error: Something went wrong - {e}", 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
