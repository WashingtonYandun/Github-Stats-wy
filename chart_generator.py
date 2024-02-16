# Color palette for the programming languages
programming_languages_palette = {
    "C": "#555555",
    "C#": "#178600",
    "C++": "#f34b7d",
    "CSS": "#563d7c",
    "HTML": "#e34c26",
    "Java": "#b07219",
    "JavaScript": "#f1e05a",
    "Objective-C": "#438eff",
    "PHP": "#4F5D95",
    "Python": "#3572A5",
    "Ruby": "#701516",
    "Rust": "#dea584",
    "Swift": "#F05138",
    "TypeScript": "#3178c6",
    "Vue": "#41b883",
    "WebAssembly": "#04133b",
    "XML": "#0060ac",
    "YAML": "#cb171e",
    "Unknown": "#222222",
    "Jupyter Notebook": "#DA5B0B",
    "TSQL": "#e38c00",
}


def generate_language_stacked_bar(username: str, lang_stats: dict) -> str:
    """
    Generate a stacked bar chart representing the language usage of a user.

    Args:
        username (str): The username of the user.
        lang_stats (dict): A dictionary containing the language statistics.
            The keys are the language names and the values are dictionaries
            containing the language statistics, including the percentage.

    Returns:
        str: The SVG template representing the stacked bar chart.
    """
    svg_padding = 20  # Padding around the entire SVG for aesthetics
    svg_width = 400  # Fixed width for simplicity
    bar_padding_horizontal = 40  # Padding inside the SVG for the bar, to not stretch fully
    bar_height = 20 # Height of each bar (language segment)
    space_above_bar = 50  # Space for the title and upper margin
    space_below_bar = 30  # Space between the bar and the legend
    legend_entry_height = 20
    legend_columns = 2  # Number of columns for the legend

    rows_per_column = (len(lang_stats) + legend_columns - 1) // legend_columns  # Calculate rows needed per column
    legend_height = rows_per_column * legend_entry_height  # Total legend height

    svg_height = space_above_bar + bar_height + space_below_bar + legend_height + svg_padding * 2  # Total SVG height

    # SVG template starts here
    svg_template = f'''
    <svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg" style="border: 1px solid #ccc; border-radius: 8px;">
        <style>
            .lang-label {{ font: 400 12px "Segoe UI", Ubuntu, Sans-Serif; fill: black; }}
            .title {{ font: bold 14px "Segoe UI", Ubuntu, Sans-Serif; fill: black; text-anchor: middle; }}
        </style>
        <text x="{svg_width / 2}" y="30" class="title">{username}'s Language Usage</text>
    '''

    total_bar_width = svg_width - bar_padding_horizontal * 2  # Width available for the bar
    current_x = bar_padding_horizontal

    for i, (lang, stats) in enumerate(sorted(lang_stats.items(), key=lambda x: x[1]['percentage'], reverse=True)):
        color = programming_languages_palette.get(lang, "#cccccc")
        width = (stats['percentage'] / 100) * total_bar_width  # Width of each segment based on percentage
        svg_template += f'<rect x="{current_x}" y="{space_above_bar}" width="{width}" height="{bar_height}" fill="{color}"/>'
        current_x += width  # Update x position for the next segment

    # Adjusting legend positioning for centered alignment
    column_width = total_bar_width / legend_columns
    start_x_offset = (svg_width - total_bar_width) / 2  # Start position for the legend to center it
    legend_start_y = space_above_bar + bar_height + space_below_bar  # Y position where the legend starts

    for i, (lang, stats) in enumerate(sorted(lang_stats.items(), key=lambda x: x[1]['percentage'], reverse=True)):
        color = programming_languages_palette.get(lang, "#cccccc")
        column_index = i % legend_columns  # Determine column based on index
        row_index = i // legend_columns  # Determine row based on index
        x_pos = start_x_offset + column_index * column_width  # X position for the legend entry
        y_pos = legend_start_y + row_index * legend_entry_height  # Y position for the legend entry

        # Add legend entries (circle and text)
        svg_template += f'''
            <circle cx="{x_pos + 10}" cy="{y_pos + 10}" r="5" fill="{color}"/>
            <text x="{x_pos + 25}" y="{y_pos + 15}" class="lang-label">{lang} {stats['percentage']}%</text>
        '''

    svg_template += '</svg>'  # Close the SVG tag
    return svg_template