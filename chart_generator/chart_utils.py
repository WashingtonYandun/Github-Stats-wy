import math

def calculate_donut_points(start_angle, end_angle, center_x, center_y, outer_radius, inner_radius):
    """
    Calculate the coordinates of the points that define a donut shape.

    Args:
        start_angle (float): The starting angle of the donut segment in degrees.
        end_angle (float): The ending angle of the donut segment in degrees.
        center_x (float): The x-coordinate of the center of the donut.
        center_y (float): The y-coordinate of the center of the donut.
        outer_radius (float): The radius of the outer circle of the donut.
        inner_radius (float): The radius of the inner circle of the donut.

    Returns:
        tuple: A tuple containing the coordinates of the start and end points of the outer and inner circles.

    Raises:
        ValueError: If an error occurs during the calculation.
    """
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