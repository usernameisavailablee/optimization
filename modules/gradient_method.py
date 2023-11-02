from datetime import time
import matplotlib
import numpy as np
from matplotlib import pyplot as plt, cm
import time
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('TkAgg')  # or 'Qt5Agg'
from sympy import *

x2, y2, z2 = symbols('x y z')
init_printing(use_unicode=True)


# получить шаг сходимости
def get_lmd():
  return 0.0008


# получить число итераций
def get_n():
  return 10


# получить начальное значение
def get_x0y0():
  return [-1, -1]


def get_function():
  x, y = symbols('x y')
  return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def __df_dx__(x, y):
  xs, ys = symbols('x y')
  df_dx = diff(get_function(), xs)
  return df_dx.subs([(xs, x), (ys, y)])


def __df_dy__(x, y):
  xs, ys = symbols('x y')
  df_dy = diff(get_function(), ys)
  return df_dy.subs([(xs, x), (ys, y)])


def __function__(x, y):
  xs, ys = symbols('x y')
  return get_function().subs([(xs, x), (ys, y)])


def start():
  # x_plt = np.arange(-2, 2, 0.01)
  # y_plt = np.arange(-2, 2, 0.01)
  # rosenbrock_plt = np.array([[__function__(x, y) for x in x_plt] for y in y_plt])
  #
  # plt.ion()  # включение интерактивного режима отображения графиков
  #
  # fig = plt.figure()
  # ax = fig.add_subplot(projection='3d')
  # x, y = np.meshgrid(x_plt, y_plt)
  # ax.plot_surface(x, y, rosenbrock_plt, rstride=20, cstride=20, cmap=cm.hot, alpha=0.6)
  #
  # ax.set_xlabel('x')
  # ax.set_ylabel('y')
  # ax.set_zlabel('rosenbrock')

  xx, yy = get_x0y0()
  # ax.scatter(xx, yy, __function__(xx, yy), c='r')
  ans_list = []
  for n in range(get_n()):
    xx = xx - get_lmd() * __df_dx__(xx, yy)
    yy = yy - get_lmd() * __df_dy__(xx, yy)
    ans_list.append([xx, yy])
    # ax.scatter(xx, yy, __function__(xx, yy), c='r')
    #
    # перерисовка графика и задержка на 10 мс
    # fig.canvas.draw()
    # fig.canvas.flush_events()
    #
    # time.sleep(0.1)
    # plt.show()

  return ans_list
  # plt.ioff()  # выключение интерактивного режима отображения графиков
  # plt.show()


start()
