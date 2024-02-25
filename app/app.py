from flask import Flask, Response, request
from services.lang_service import lang_service

app = Flask(__name__)

@app.route('/langs/<username>/<chart>', methods=['GET'])
def langs(username: str, chart: str) -> Response:
    try:
        svg_image = lang_service(username, chart, request.args)
        return Response(svg_image, mimetype='image/svg+xml')
    except Exception as e:
        return f"Error: Something went wrong - {e}", 500


@app.route('/', methods=['GET'])
def index() -> dict:
    return {
        'message': 'Give a star to the project if you liked it! In the future this will be a landing page with some information about the project and how to use it.',
        'endpoints': {
            'get_language_stats_chart': '/langs/<username>/<chart>'
        }
    }