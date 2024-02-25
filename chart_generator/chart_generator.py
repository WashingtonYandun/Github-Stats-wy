import math
from chart_generator.palettes import programming_languages_palette
from chart_generator.chart_utils import calculate_donut_points
from stats_calculator.langs_stats_calculator import get_top_n_langs

def generate_language_stacked_bar(
        username: str,
        lang_stats: dict,
        chart_kwargs: dict
        ) -> str:
    
    try:
        # Unpack chart_kwargs
        border_color = chart_kwargs.get('border_color', "#cccccc")
        background_color = chart_kwargs.get('background_color', "#ffffff")
        title_color = chart_kwargs.get('title_color', "#000000")
        text_color = chart_kwargs.get('text_color', "#000000")
        border_radius = chart_kwargs.get('border_radius', 10)

        # Adjusted parameters
        svg_padding = 15
        border_width = 1
        svg_width = 400
        bar_padding_horizontal = 30
        bar_height = 20
        space_above_bar = 40
        space_below_bar = 25
        legend_entry_height = 18
        legend_columns = 2

        # Process top 7 languages and 'Others'
        top_langs = get_top_n_langs(lang_stats, 7)

        # Calculate legend height and total SVG height
        rows_per_column = (len(top_langs) + legend_columns - 1) // legend_columns
        legend_height = rows_per_column * legend_entry_height
        svg_height = space_above_bar + bar_height + space_below_bar + legend_height + svg_padding * 2

        # SVG template initialization with a border rectangle
        svg_template = f'''
        <svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect width="{svg_width}" height="{svg_height}" fill="{background_color}" rx="{border_radius}"/>
            <rect x="{border_width / 2}" y="{border_width / 2}" width="{svg_width - border_width}" height="{svg_height - border_width}" fill="none" stroke="{border_color}" stroke-width="{border_width}" rx="{border_radius - border_width / 2}"/>
            <style>
                .lang-label {{ font: 400 12px "Segoe UI", Ubuntu, Sans-Serif; fill: {text_color}; }}
                .title {{ font: bold 14px "Segoe UI", Ubuntu, Sans-Serif; fill: {title_color}; text-anchor: middle; }}
            </style>
            <text x="{svg_width / 2}" y="30" class="title">{username}'s Language Usage</text>
        '''

        # Generate the bar segments
        total_bar_width = svg_width - bar_padding_horizontal * 2
        current_x = bar_padding_horizontal
        for lang, stats in top_langs.items():
            color = programming_languages_palette.get(lang, "#cccccc")
            width = (stats['percentage'] / 100) * total_bar_width
            svg_template += f'<rect x="{current_x}" y="{space_above_bar}" width="{width}" height="{bar_height}" fill="{color}"/>'
            current_x += width

        # Generate the legend
        column_width = total_bar_width / legend_columns
        start_x_offset = (svg_width - total_bar_width) / 2
        legend_start_y = space_above_bar + bar_height + space_below_bar
        for i, (lang, stats) in enumerate(top_langs.items()):
            color = programming_languages_palette.get(lang, "#cccccc") if lang != 'Others' else "#cccccc"
            column_index = i % legend_columns
            row_index = i // legend_columns
            x_pos = start_x_offset + column_index * column_width
            y_pos = legend_start_y + row_index * legend_entry_height
            svg_template += f'''
                <circle cx="{x_pos + 10}" cy="{y_pos + 10}" r="5" fill="{color}"/>
                <text x="{x_pos + 25}" y="{y_pos + 15}" class="lang-label">{lang} {stats['percentage']}%</text>
            '''
        
        svg_template += '</svg>'
        return svg_template
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with generate_language_stacked_bar - {e}")


def generate_language_donut_chart(
        username: str,
        lang_stats: dict,
        chart_kwargs: dict
        ) -> str:
    
    try:
        # Unpack chart_kwargs
        border_color = chart_kwargs.get('border_color', "#cccccc")
        background_color = chart_kwargs.get('background_color', "#ffffff")
        title_color = chart_kwargs.get('title_color', "#000000")
        text_color = chart_kwargs.get('text_color', "#000000")
        hole_radius_percentage = chart_kwargs.get('hole_radius_percentage', 40)
        border_radius = chart_kwargs.get('border_radius', 10)
        border_width = 1

        # Process top 6 languages and others
        top_langs = get_top_n_langs(lang_stats, 6).items()

        # Constants for the SVG
        svg_width = 398
        svg_height = 198
        outer_radius = 60
        inner_radius = (hole_radius_percentage / 100) * outer_radius
        chart_center_x = svg_width / 3
        chart_center_y = svg_height / 2
        legend_x_start = 2 * svg_width / 3 - 40
        legend_y_start = (svg_height - (len(top_langs) * 20)) / 2 + 10

        # Initialize SVG template with rounded corners
        svg_template = f'''
        <svg width="{svg_width}" height="{svg_height}" viewBox="0 0 {svg_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">
            <rect width="{svg_width}" height="{svg_height}" fill="{background_color}" rx="{border_radius}"/>
            <rect x="{border_width / 2}" y="{border_width / 2}" width="{svg_width - border_width}" height="{svg_height - border_width}" fill="none" stroke="{border_color}" stroke-width="{border_width}" rx="{border_radius - border_width / 2}"/>
            <style>
                .title {{ font: bold 14px "Segoe UI", Ubuntu, Sans-Serif; fill: {title_color}; text-anchor: middle; }}
                .lang-label {{ font: 400 12px "Segoe UI", Ubuntu, Sans-Serif; fill: {text_color}; }}
            </style>
            <text x="{svg_width / 2}" y="20" class="title">{username}'s Language Usage</text>
        '''

        # Generate the donut chart
        start_angle = 0
        for lang, stats in top_langs:
            color = programming_languages_palette.get(lang, "#cccccc")
            percentage = stats['percentage']
            sweep_angle = (percentage / 100) * 360
            end_angle = start_angle + sweep_angle

            start_point_outer, end_point_outer, start_point_inner, end_point_inner = calculate_donut_points(
                start_angle, end_angle, chart_center_x, chart_center_y, outer_radius, inner_radius)

            large_arc_flag = '1' if sweep_angle > 180 else '0'

            path_d = f"M {start_point_outer[0]} {start_point_outer[1]} A {outer_radius} {outer_radius} 0 {large_arc_flag} 1 {end_point_outer[0]} {end_point_outer[1]} L {end_point_inner[0]} {end_point_inner[1]} A {inner_radius} {inner_radius} 0 {large_arc_flag} 0 {start_point_inner[0]} {start_point_inner[1]} Z"
            svg_template += f'<path d="{path_d}" fill="{color}"/>'

            start_angle += sweep_angle

        # Add legend
        for i, (lang, stats) in enumerate(top_langs):
            color = programming_languages_palette.get(lang, "#cccccc")
            y_pos = legend_y_start + (i * 20)

            svg_template += f'''
                <rect x="{legend_x_start}" y="{y_pos}" width="10" height="10" fill="{color}"/>
                <text x="{legend_x_start + 15}" y="{y_pos + 10}" class="lang-label">{lang} ({stats['percentage']}%)</text>
            '''

        svg_template += '</svg>'
        return svg_template
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with generate_language_donut_chart - {e}")
