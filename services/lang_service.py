from factory.chart_factory import chart_factory
from github_api.github_api import get_user_repos
from stats_calculator.langs_stats_calculator import calculate_language_stats
from utils.utils import extract_chart_kwargs


def lang_service(username: str, chart_type: str, query_params: dict) -> str:
    """
    Retrieves the language statistics for a given user's repositories and generates a chart based on the specified chart type.

    Args:
        username (str): The username of the GitHub user.
        chart_type (str): The type of chart to generate (e.g., 'bar', 'pie', 'donut').
        query_params (dict): Additional query parameters for customizing the chart.

    Returns:
        str: The generated chart as a string.

    Raises:
        ValueError: If an error occurs during the execution of the lang_service function.
    """
    try:
        repos = get_user_repos(username)
        lang_stats = calculate_language_stats(repos)

        if 'error_message' in lang_stats:
            raise Exception(lang_stats['error_message'])

        chart_kwargs = extract_chart_kwargs(query_params, chart_type)
        
        return chart_factory(username, lang_stats, chart_type, chart_kwargs)
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with lang_service - {e}")