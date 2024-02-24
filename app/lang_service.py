from app.utils import build_chart_kwargs
from factory.chart_factory import chart_factory
from github_api.github_api import get_user_repos
from stats_calculator.langs_stats_calculator import calculate_language_stats


def get_language_stats_chart(username, chart, args):
    def handle_error(e):
        return f"Error: Something went wrong - {e}", 500

    def process_stats(lang_stats):
        if 'error_message' in lang_stats:
            return lang_stats['error_message'], 500

        chart_kwargs = build_chart_kwargs(args, chart)
        return chart_factory(username, lang_stats, chart, chart_kwargs)

    try:
        repos = get_user_repos(username)
        lang_stats = calculate_language_stats(repos)
        return process_stats(lang_stats)
    except Exception as e:
        return handle_error(e)