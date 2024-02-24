from flask import Flask, Response, request
from app.lang_service import get_language_stats_chart
from factory.chart_factory import chart_factory
from github_api.github_api import get_user_repos
from stats_calculator.langs_stats_calculator import calculate_language_stats

app = Flask(__name__)

@app.route('/langs/<username>/<chart>', methods=['GET'])
def langs(username: str, chart: str) -> Response:
    return get_language_stats_chart(username, chart, request.args)


@app.route('/', methods=['GET'])
def index() -> dict:
    return {
        'message': 'Give a star to the project if you liked it! In the future this will be a landing page with some information about the project and how to use it.',
        'endpoints': {
            'get_language_stats_chart': '/langs/<username>/<chart>'
        }
    }