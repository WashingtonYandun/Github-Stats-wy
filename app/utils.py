def add_hash(color_value: str) -> str:
    return f"#{color_value}" if not color_value.startswith('#') else color_value

def build_chart_kwargs(args, chart_type):
    chart_kwargs = {
        'border_color': add_hash(args.get('border_color', 'E4E2E2')),
        'background_color': add_hash(args.get('background_color', 'fff')),
        'title_color': add_hash(args.get('title_color', '000')),
        'text_color': add_hash(args.get('text_color', '000')),
        'hole_radius_percentage': args.get('hole_radius_percentage', default=40, type=int)
    }

    if chart_type == 'pie':
        chart_kwargs['hole_radius_percentage'] = 0

    return chart_kwargs
