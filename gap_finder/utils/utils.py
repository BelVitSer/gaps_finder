__all__ = [
    'find_equation_plane_rates',
    'get_triangle_square_from_three_cords'
]


def get_triangle_square_from_three_cords(coord1, coord2, coord3) -> float:
    """
    Площадь треугольника по трём кординатам


    :param coord1:
    :param coord2:
    :param coord3:

    :return: (float) S - площадь треугольника
    """
    x1, y1, _ = coord1
    x2, y2, _ = coord2
    x3, y3, _ = coord3
    S = 0.5 * abs(((x1 - x3) * (y2 - y3)) - ((x2 - x3) * (y1 - y3)))
    return S


def find_equation_plane_rates(x1, y1, z1, x2, y2, z2, x3, y3, z3) -> (int, int, int, int):
    """
    Функция находит коэффициенты уравнения плоскости по трем точкам,
    принимая координаты этих трёх точек.

    # TODO Форматирование докстрингов почитать

    :param x1: Координата x точки #1
    :param y1: Координата y точки #1
    :param z1:  Координата z точки #1
    :param x2: Координата x точки #2
    :param y2: Координата y точки #2
    :param z2:  Координата z точки #2
    :param x3: Координата x точки #3
    :param y3: Координата y точки #3
    :param z3:  Координата z точки #3

    :return: a, b, c, d
    """
    a1 = x2 - x1
    b1 = y2 - y1
    c1 = z2 - z1
    a2 = x3 - x1
    b2 = y3 - y1
    c2 = z3 - z1
    a = b1 * c2 - b2 * c1
    b = a2 * c1 - a1 * c2
    c = a1 * b2 - b1 * a2
    d = (- a * x1 - b * y1 - c * z1)

    # print("equation of plane is ", a, "x +", b, "y +", c, "z +", d, "= 0.")

    return a, b, c, d
