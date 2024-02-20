from flask import Flask, Response, request
from app.chart_factory import chart_factory
from github_api.github_api import get_user_repos
from stats_calculator.stats_calculator import calculate_language_stats

app = Flask(__name__)

@app.route('/langs/<username>/<chart>', methods=['GET'])
def langs(username: str, chart: str) -> Response:
    """
    Retrieves the language statistics for a given GitHub user's repositories and generates a chart based on the provided type.

    Args:
        username (str): The GitHub username.
        chart (str): The type of chart to generate.

    Returns:
        Response: The generated chart image in SVG format.

    Raises:
        Exception: If an error occurs during the process.
    """
    try:
        repos = get_user_repos(username)
        lang_stats = calculate_language_stats(repos)

        if 'error_message' in lang_stats:
            return lang_stats['error_message'], 500
        
        chart_kwargs = {
            'border_color': request.args.get('border_color', default='#fff', type=str),
            'background_color': request.args.get('background_color', default='#fff', type=str),
            'title_color': request.args.get('title_color', default='#000', type=str),
            'text_color': request.args.get('text_color', default='#000', type=str),
        }

        if chart == 'donut':
            chart_kwargs['hole_radius_percentage'] = request.args.get('hole_radius_percentage', default=40, type=int)
        elif chart == 'pie':
            chart_kwargs['hole_radius_percentage'] = 0

        svg_image = chart_factory(username, lang_stats, chart, **chart_kwargs)

        return Response(svg_image, mimetype='image/svg+xml')

    except Exception as e:
        return f"Error: Something went wrong - {e}", 500
    

@app.route('/')
def index() -> str:
    return {
        "Langs Usage": "https://github-stats-wy.vercel.app/langs/<username"
    }
