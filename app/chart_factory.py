

from chart_generator.chart_generator import generate_language_donut_chart, generate_language_stacked_bar


def chart_factory(username : str, lang_stats: dict, chart_type: str, chart_kwargs: dict):
    """
    Factory function to generate different types of charts based on the given chart type.

    Args:
        username (str): The username for which the chart is generated.
        lang_stats (dict): The language statistics for the user.
        chart_type (str): The type of chart to generate ('pie', 'bar', or 'donut').
        chart_kwargs (dict): Additional keyword arguments for chart generation.

    Returns:
        The generated chart based on the given chart type.

    Raises:
        ValueError: If an invalid chart type is provided.
    """
    if chart_type == 'pie':
        return generate_language_donut_chart(username=username, lang_stats=lang_stats, chart_kwargs=chart_kwargs)
    elif chart_type == 'bar':
        return generate_language_stacked_bar(username=username, lang_stats=lang_stats, chart_kwargs=chart_kwargs)
    elif chart_type == 'donut':
        return generate_language_donut_chart(username=username, lang_stats=lang_stats, chart_kwargs=chart_kwargs)
    else:
        raise ValueError("Invalid chart type provided.")
