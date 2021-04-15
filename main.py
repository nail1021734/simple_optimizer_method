import _1Dsearch as oneDim
import _cyclic as cyclic
import _powell_method as powell
import matplotlib.pyplot as plt
from math import sin, cos
import numpy as np


def plot_func(f, lb, ub, filename):
    x, y = [], []
    for i in np.arange(lb, ub, 0.01):
        x.append(i)
        y.append(f(i))
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(f'python_code/result_plot/{filename}')
    plt.clf()


def Q1():

    def f(x): return (x**2 * sin(x) * cos(x))

    plot_func(f=f, lb=2, ub=6, filename="Q1_function.png")
    result = oneDim.goldSearch(
        func=f,
        a=2,
        b=6,
        tol=1e-5
    )
    print(f'golden search: min_value={result["y"]}, min_point={result["X"]}')
    y_list = [f(x) for x in result['x_list']]
    plt.plot(range(len(y_list)), y_list)
    plt.savefig('python_code/result_plot/gold.png')
    plt.clf()

    result = oneDim.Dichotomous(
        func=f,
        a=2,
        b=6,
        ep=1e-6,
        tol=1e-5
    )
    y_list = [f(x) for x in result['x_list']]
    print(
        f'Dichotomous search: min_value={result["y"]}, min_point={result["X"]}')
    # plt.plot(range(len(y_list)), y_list)
    plt.scatter(range(len(y_list)), y_list)
    plt.savefig('python_code/result_plot/Dichotomous.png')
    plt.clf()


def Q2():

    def f(x: list): return (4 - 2.1 * x[0]**2 + (x[0]**4) / 3) * \
        x[0]**2 + x[0] * x[1] + (-4 + 4 * x[1]**2) * x[1]**2

    result = cyclic.cyclic(
        func=f,
        init_X=[-1, 1],
        x_bound_list=[[-2, 2], [-2, 2]],
        tol=1e-3
    )
    print(
        f'cyclic coordinate method: min_value={result["y"]}, min_point={result["X"]}')
    x, y = zip(*result['x_list'])
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(x, y, color='red')
    plt.savefig('python_code/result_plot/cyclic.png')
    plt.clf()


def Q3():

    def f(x): return (4 - 2.1 * x[0]**2 + (x[0]**4) / 3) * \
        x[0]**2 + x[0] * x[1] + (-4 + 4 * x[1]**2) * x[1]**2

    result = powell.powell(
        func=f,
        X=np.array([-1, -1]),
        min_b=-2,
        max_b=2,
        tol=1e-5
    )
    x, y = zip(*result['x_list'])
    print(
        f'powell\'s method: min_value={result["y"]}, min_point={result["X"]}')
    plt.plot(x, y)
    # plt.scatter(x, y, color='red')
    plt.savefig('python_code/result_plot/powell.png')


def main():
    Q1()
    Q2()
    Q3()


if __name__ == "__main__":
    main()
