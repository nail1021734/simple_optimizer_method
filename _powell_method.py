import numpy as np


def goldSearch(func, d, cur_pos, min_b, max_b, tol):
    R = (3 - 5**0.5) / 2
    x1 = min_b + (max_b - min_b) * R
    x2 = min_b + max_b - x1

    f1 = func(cur_pos + x1 * d)
    f2 = func(cur_pos + x2 * d)

    while max_b - min_b > tol:
        if f1 < f2:
            max_b, x2, f2 = x2, x1, f1
            x1 = min_b + R * (max_b - min_b)
            f1 = func(cur_pos + x1 * d)
            min_x = x1
        else:
            min_b, x1, f1 = x1, x2, f2
            x2 = max_b - R * (max_b - min_b)
            f2 = func(cur_pos + x2 * d)
            min_x = x2

    return {'X': min_x, 'y': func(cur_pos + min_x * d)}


def powell(func, X, min_b, max_b, tol):
    dim = X.size
    d = np.eye(dim)
    new_x = None

    min_x_list = [X]
    while new_x is None or np.max(np.abs(X - new_x)) > tol:
        cur_pos = X

        for i in range(dim):
            result = goldSearch(
                func=func,
                d=d[:, i],
                cur_pos=cur_pos,
                min_b=min_b - cur_pos[0],
                max_b=max_b - cur_pos[1],
                tol=tol
            )
            lmb = result['X']
            cur_pos = cur_pos + lmb * d[:, i]
            min_x_list.append(cur_pos)

        for i in range(dim - 1):
            d[:, i] = d[:, i + 1]
        d[:, dim - 1] = cur_pos - X
        d[:, dim - 1] = d[:, dim - 1] / np.linalg.norm(d[:, dim - 1], ord=2)

        new_x = X
        result = goldSearch(
            func=func,
            d=d[:, dim - 1],
            cur_pos=cur_pos,
            min_b=min_b - cur_pos[0],
            max_b=max_b - cur_pos[1],
            tol=tol
        )
        lmb = result['X']
        X = cur_pos + lmb * d[:, dim - 1]
        min_x_list.append(X)
    min_y = func(X)

    return {'X': X, 'y': min_y, 'x_list': min_x_list}
