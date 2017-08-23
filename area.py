def circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area


def square_area(length):
    area = (length ** 2)
    return area


def points_distance(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    dist = ((dx ** 2) + (dy ** 2)) ** 0.5
    print dist
    return dist
