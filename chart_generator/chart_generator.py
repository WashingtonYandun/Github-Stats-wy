import math
from chart_generator.palettes import programming_languages_palette

def generate_language_stacked_bar(
        username: str,
        lang_stats: dict,
        chart_kwargs: dict
        ) -> str:
 
    # Unpack chart_kwargs
    border_color = chart_kwargs.get('border_color', "#cccccc")
    background_color = chart_kwargs.get('background_color', "#ffffff")
    title_color = chart_kwargs.get('title_color', "#000000")
    text_color = chart_kwargs.get('text_color', "#000000")

    # Adjusted parameters for a more compact and customized chart
    svg_padding = 15
    svg_width = 400
    bar_padding_horizontal = 30
    bar_height = 20
    space_above_bar = 40
    space_below_bar = 25
    legend_entry_height = 18
    legend_columns = 2

    # Calculate legend height and total SVG height
    rows_per_column = (len(lang_stats) + legend_columns - 1) // legend_columns
    legend_height = rows_per_column * legend_entry_height
    svg_height = space_above_bar + bar_height + space_below_bar + legend_height + svg_padding * 2

    # SVG template initialization
    svg_template = f'''
    <svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg" style="border: 1px solid {border_color}; border-radius: 8px; background-color: {background_color};">
        <style>
            .lang-label {{ font: 400 12px "Segoe UI", Ubuntu, Sans-Serif; fill: {text_color}; }}
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
    
    svg_template += '</svg>'
    return svg_template


def generate_language_donut_chart(
        username: str,
        lang_stats: dict,
        chart_kwargs: dict
        ) -> str:

    # Unpack chart_kwargs
    border_color = chart_kwargs.get('border_color', "#cccccc")
    background_color = chart_kwargs.get('background_color', "#ffffff")
    title_color = chart_kwargs.get('title_color', "#000000")
    text_color = chart_kwargs.get('text_color', "#000000")
    hole_radius_percentage = chart_kwargs.get('hole_radius_percentage', 40)

    svg_width = 400
    svg_height = 200
    radius = 60
    hole_radius = (hole_radius_percentage / 100) * radius
    chart_center_x = svg_width / 3  # Position chart on the left
    chart_center_y = svg_height / 2  # Center chart vertically 
    legend_x_start = 2 * svg_width / 3 - 50  # Adjust legend position for compactness (50 is important for the legend to be centered)
    legend_y_start = (svg_height - (len(lang_stats) * 20)) / 2 + 10  # Center legend vertically, adjusted for compactness

    # SVG template initialization with border
    svg_template = f'''
    <svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg" style="border: 1px solid {border_color}; background-color: {background_color};">
        <style>
            .title {{ font: bold 14px "Segoe UI", Ubuntu, Sans-Serif; fill: {title_color}; text-anchor: middle; }}
            .lang-label {{ font: 400 12px "Segoe UI", Ubuntu, Sans-Serif; fill: {text_color}; }}
        </style>
        <text x="{svg_width / 2}" y="20" class="title">{username}'s Language Usage</text>
    '''

    # Calculate the start and end angles for each slice and draw them
    start_angle = 0
    for lang, stats in lang_stats.items():
        color = programming_languages_palette.get(lang, "#cccccc")
        percentage = stats['percentage']
        sweep_angle = (percentage / 100) * 360
        end_angle = start_angle + sweep_angle

        # Draw donut slices
        start_point_outer = (
            chart_center_x + radius * math.cos(math.radians(start_angle)),
            chart_center_y + radius * math.sin(math.radians(start_angle))
        )
        end_point_outer = (
            chart_center_x + radius * math.cos(math.radians(end_angle)),
            chart_center_y + radius * math.sin(math.radians(end_angle))
        )
        start_point_inner = (
            chart_center_x + hole_radius * math.cos(math.radians(start_angle)),
            chart_center_y + hole_radius * math.sin(math.radians(start_angle))
        )
        end_point_inner = (
            chart_center_x + hole_radius * math.cos(math.radians(end_angle)),
            chart_center_y + hole_radius * math.sin(math.radians(end_angle))
        )

        large_arc_flag = 1 if sweep_angle > 180 else 0

        path_d = f"M {start_point_outer[0]} {start_point_outer[1]} \
                   A {radius} {radius} 0 {large_arc_flag} 1 {end_point_outer[0]} {end_point_outer[1]} \
                   L {end_point_inner[0]} {end_point_inner[1]} \
                   A {hole_radius} {hole_radius} 0 {large_arc_flag} 0 {start_point_inner[0]} {start_point_inner[1]} Z"
        svg_template += f'<path d="{path_d}" fill="{color}"/>'

        start_angle += sweep_angle

    # Add legend on the right side, compactly
    for i, (lang, stats) in enumerate(lang_stats.items()):
        color = programming_languages_palette.get(lang, "#cccccc")
        y_pos = legend_y_start + (i * 20)

        svg_template += f'''
            <rect x="{legend_x_start}" y="{y_pos}" width="10" height="10" fill="{color}"/>
            <text x="{legend_x_start + 15}" y="{y_pos + 10}" class="lang-label">{lang} ({stats['percentage']}%)</text>
        '''

    svg_template += '</svg>'
    return svg_template
