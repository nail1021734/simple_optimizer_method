from math import sin, cos


def f(x):
    return x**2 * sin(x) * cos(x)


def goldSearch(func, a, b, tol):
    R = (5**0.5 - 1) / 2
    C = 1 - R

    x1 = R * a + C * b
    x2 = C * a + R * b
    y1 = func(x1)
    y2 = func(x2)

    min_x_list = []
    while (b - a) > tol:
        if y1 > y2:
            a, x1, y1 = x1, x2, y2
            x2 = C * a + R * b
            y2 = func(x2)
            min_x = x2
        else:
            b, x2, y2 = x2, x1, y1
            x1 = R * a + C * b
            y1 = func(x1)
            min_x = x1
        min_x_list.append(min_x)

    return {'y': func(min_x), 'X': min_x, 'x_list': min_x_list}


def Dichotomous(func, a, b, ep, tol):

    if 2 * ep > tol:
        raise ValueError("2 * eps should small than tol.")

    min_x_list = []
    while (b - a) > tol:
        mid = (a + b) / 2

        min_x_list.append(mid)
        if func(mid - ep) < func(mid + ep):
            b = mid + ep
        else:
            a = mid - ep
    min_x = (a + b) / 2
    min_y = func(min_x)
    min_x_list.append(min_x)

    return {'y': min_y, 'X': min_x, 'x_list': min_x_list}
