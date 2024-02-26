from chart_generator.palettes import wy_palettes

# TODO: REFAC: Refactor the following functions use a validation function for the chart_kwargs

def extract_chart_kwargs(query_params: dict, chart_type: str) -> dict:
    """
    Extracts chart keyword arguments from the given query parameters and chart type.

    Args:
        query_params (dict): The query parameters containing the chart options.
        chart_type (str): The type of chart.

    Returns:
        dict: The chart keyword arguments.

    Raises:
        ValueError: If an error occurs during the extraction process.
    """
    try:
        chart_kwargs = {
            'border_color': add_hash(query_params.get('border_color', default='E4E2E2', type=str)),
            'background_color': add_hash(query_params.get('background_color', default='fff', type=str)),
            'title_color': add_hash(query_params.get('title_color', default='000', type=str)),
            'text_color': add_hash(query_params.get('text_color', default='000', type=str)),
            'hole_radius_percentage': query_params.get('hole_radius_percentage', default=40, type=int),
            'border_radius': query_params.get('border_radius', default=10, type=int),
            "bar_height": query_params.get('bar_height', default=20, type=int),
            "outer_radius": query_params.get('outer_radius', default=100, type=int),
            "border_width": query_params.get('border_width', default=1, type=int),
            "palette": query_params.get('palette', default='None', type=str),
        }

        if chart_type == 'pie':
            chart_kwargs['hole_radius_percentage'] = 0

        if chart_type == 'donut' and (chart_kwargs['hole_radius_percentage'] >= 100 or chart_kwargs['hole_radius_percentage'] < 0):
            chart_kwargs['hole_radius_percentage'] = 40

        if chart_kwargs['border_width'] >= 200 or chart_kwargs['border_width'] < 0:
            chart_kwargs['border_width'] = 1

        if chart_kwargs["outer_radius"] >= 60 or chart_kwargs["outer_radius"] < 0:
            chart_kwargs["outer_radius"] = 60

        if chart_kwargs["bar_height"] >= 25 or chart_kwargs["bar_height"] < 0:
            chart_kwargs["bar_height"] = 20

        if chart_kwargs["palette"] not in wy_palettes:
            chart_kwargs["palette"] = 'None'


        return chart_kwargs
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with extract_chart_kwargs - {e}")
    

def add_hash(color_value: str) -> str:
    """
    Adds a '#' character at the beginning of the color value if it doesn't already have one.

    Args:
        color_value (str): The color value to add the '#' character to.

    Returns:
        str: The color value with the '#' character added.

    Raises:
        ValueError: If an error occurs while adding the '#' character.
    """
    try:
        if not color_value.startswith('#'):
            color_value = f"#{color_value}"
        return color_value
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with add_hash - {e}")