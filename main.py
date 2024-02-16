import os
from flask import Flask, Response, request
from github_api import get_user_repos
from stats_calculator import calculate_language_stats
from chart_generator import generate_language_stacked_bar, generate_language_pie_chart, generate_language_donut_chart

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
        svg_image = None

        if 'error_message' in lang_stats:
            return lang_stats['error_message'], 500
        
        border_color = request.args.get('border_color', default='#fff', type=str)
        background_color = request.args.get('background_color', default='#fff', type=str)
        title_color = request.args.get('title_color', default='#000', type=str)
        text_color = request.args.get('text_color', default='#000', type=str)
        

        if chart == 'pie':
            svg_image = generate_language_pie_chart(
                username=username,
                lang_stats=lang_stats,
                
                border_color=border_color,
                background_color=background_color,
                title_color=title_color,
                text_color=text_color
                )
            
        elif chart == 'bar':
            svg_image = generate_language_stacked_bar(
                username=username,
                lang_stats=lang_stats,

                border_color=border_color,
                background_color=background_color,
                title_color=title_color,
                text_color=text_color
                )

        elif chart == 'donut':
            hole_radius_percentage = request.args.get('hole_radius_percentage', default=40, type=int)
            svg_image = generate_language_donut_chart(
                username=username,
                lang_stats=lang_stats,
                border_color=border_color,
                background_color=background_color,
                title_color=title_color,
                text_color=text_color,
                hole_radius_percentage=hole_radius_percentage
                )

        return Response(svg_image, mimetype='image/svg+xml')

    except Exception as e:
        return f"Error: Something went wrong - {e}", 500
    

@app.route('/')
def index() -> str:
    return {
        "Langs Usage": "https://github-stats-wy.vercel.app/langs/<username>/<chart>&border_color=<color>&background_color=<color>&title_color=<color>&text_color=<color>&hole_radius_percentage=<int>",
        "Profile Usage": "https://github-stats-wy.vercel.app/profile/<username>&border_color=<color>&background_color=<color>&title_color=<color>&text_color=<color>"
    }


    

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
