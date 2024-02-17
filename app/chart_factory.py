

from chart_generator.chart_generator import generate_language_donut_chart, generate_language_pie_chart, generate_language_stacked_bar


def chart_factory(username, lang_stats, chart_type, **kwargs):
    """
    Factory method for generating different types of language charts.

    Args:
        username (str): The GitHub username.
        lang_stats (dict): Language statistics for user repositories.
        chart_type (str): The type of chart to generate.
        **kwargs: Additional arguments for customization.

    Returns:
        str: The generated chart image in SVG format.
    """
    if chart_type == 'pie':
        return generate_language_pie_chart(username=username, lang_stats=lang_stats, **kwargs)
    elif chart_type == 'bar':
        return generate_language_stacked_bar(username=username, lang_stats=lang_stats, **kwargs)
    elif chart_type == 'donut':
        return generate_language_donut_chart(username=username, lang_stats=lang_stats, **kwargs)
