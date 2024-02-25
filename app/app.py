from flask import Flask, Response, request
from services.lang_service import lang_service

app = Flask(__name__)

@app.route('/langs/<username>/<chart>', methods=['GET'])
def langs(username: str, chart: str) -> Response:
    """
    Retrieve the language statistics for a given user and generate an SVG chart.

    Args:
        username (str): The username of the GitHub user.
        chart (str): The type of chart to generate. Valid options are 'bar', 'pie', and 'donut'.

    Returns:
        Response: The SVG chart image as a Flask Response object.

    Raises:
        Exception: If an error occurs during the process.
    """
    try:
        svg_image = lang_service(username, chart, request.args)
        return Response(svg_image, mimetype='image/svg+xml')
    except Exception as e:
        return f"Error: Something went wrong - {e}", 500
