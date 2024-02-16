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


def generate_language_stacked_bar(
        username: str,
        lang_stats: dict,
        border_color: str = "#cccccc",
        background_color: str = "#ffffff",
        title_color: str = "#000000",
        percentage_color: str = "#000000"
        ) -> str:
    """
    Generate a compact stacked bar chart representing the language usage of a user with customizable color options.

    Args:
        username (str): The username of the user.
        lang_stats (dict): A dictionary containing the language statistics, including the percentage.
        border_color (str): Hex color for the SVG border.
        background_color (str): Hex color for the SVG background.
        title_color (str): Hex color for the title text.
        percentage_color (str): Hex color for the percentage text.

    Returns:
        str: The SVG template representing the stacked bar chart.
    """
    # Adjusted parameters for a more compact and customized chart
    svg_padding = 15  # Reduced padding
    svg_width = 350  # Reduced width for compactness
    bar_padding_horizontal = 30  # Adjusted padding inside SVG for the bar
    bar_height = 20  # Height of each bar (language segment)
    space_above_bar = 40  # Reduced space for title
    space_below_bar = 25  # Reduced space for legend
    legend_entry_height = 18  # Slightly reduced for compactness
    legend_columns = 2  # Number of columns for the legend remains the same

    # Calculate legend height and total SVG height
    rows_per_column = (len(lang_stats) + legend_columns - 1) // legend_columns
    legend_height = rows_per_column * legend_entry_height
    svg_height = space_above_bar + bar_height + space_below_bar + legend_height + svg_padding * 2

    # SVG template initialization
    svg_template = f'''
    <svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg" style="border: 1px solid {border_color}; border-radius: 8px; background-color: {background_color};">
        <style>
            .lang-label {{ font: 400 12px "Segoe UI", Ubuntu, Sans-Serif; fill: {percentage_color}; }}
            .title {{ font: bold 14px "Segoe UI", Ubuntu, Sans-Serif; fill: {title_color}; text-anchor: middle; }}
        </style>
        <text x="{svg_width / 2}" y="30" class="title">{username}'s Language Usage</text>
    '''

    # Calculate total bar width and initialize current_x position
    total_bar_width = svg_width - bar_padding_horizontal * 2 # Width minus the padding (Available space for the bars)
    current_x = bar_padding_horizontal

    # Loop through language statistics to create bar segments
    for lang, stats in sorted(lang_stats.items(), key=lambda x: x[1]['percentage'], reverse=True):
        color = programming_languages_palette.get(lang, "#cccccc")
        width = (stats['percentage'] / 100) * total_bar_width # Calculate the width based on the percentage
        svg_template += f'<rect x="{current_x}" y="{space_above_bar}" width="{width}" height="{bar_height}" fill="{color}"/>'
        current_x += width # Update the current_x position for the next segment

    # Calculate legend column width, start_x_offset, and legend_start_y
    column_width = total_bar_width / legend_columns
    start_x_offset = (svg_width - total_bar_width) / 2 # Start position for the legend entries to be centered
    legend_start_y = space_above_bar + bar_height + space_below_bar # Y position for the first legend entry

    # Loop through language statistics to create legend entries
    for i, (lang, stats) in enumerate(sorted(lang_stats.items(), key=lambda x: x[1]['percentage'], reverse=True)):
        color = programming_languages_palette.get(lang, "#cccccc")
        column_index = i % legend_columns # Determine the column based on the index
        row_index = i // legend_columns # Determine the row based on the index
        x_pos = start_x_offset + column_index * column_width # X position for the current entry
        y_pos = legend_start_y + row_index * legend_entry_height # Y position for the current entry

        svg_template += f'''
            <circle cx="{x_pos + 10}" cy="{y_pos + 10}" r="5" fill="{color}"/>
            <text x="{x_pos + 25}" y="{y_pos + 15}" class="lang-label">{lang} {stats['percentage']}%</text>
        '''

    # Close the SVG template
    svg_template += '</svg>'
    return svg_template
