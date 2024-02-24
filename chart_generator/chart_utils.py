import math

def calculate_donut_points(start_angle, end_angle, center_x, center_y, outer_radius, inner_radius):
    try:
        start_point_outer = (
            center_x + outer_radius * math.cos(math.radians(start_angle)),
            center_y + outer_radius * math.sin(math.radians(start_angle))
        )
        end_point_outer = (
            center_x + outer_radius * math.cos(math.radians(end_angle)),
            center_y + outer_radius * math.sin(math.radians(end_angle))
        )
        start_point_inner = (
            center_x + inner_radius * math.cos(math.radians(start_angle)),
            center_y + inner_radius * math.sin(math.radians(start_angle))
        )
        end_point_inner = (
            center_x + inner_radius * math.cos(math.radians(end_angle)),
            center_y + inner_radius * math.sin(math.radians(end_angle))
        )
        return start_point_outer, end_point_outer, start_point_inner, end_point_inner
    except Exception as e:
        raise ValueError(f"Error: Something went wrong with calculate_donut_points - {e}")