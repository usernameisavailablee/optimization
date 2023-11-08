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

def get_eps():
  return 1

# получить число итераций
def get_n():
  return 1000


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


  xx_new, yy_new = get_x0y0()
  f_value_new = __function__(xx_new, yy_new)
  ans_list = []

  for n in range(get_n()):
    xx_old = xx_new
    yy_old = yy_new
    f_value_old = f_value_new

    ans_list.append([xx_old, yy_old])

    xx_new = xx_old - get_lmd() * __df_dx__(xx_old, yy_old)
    yy_new = yy_old - get_lmd() * __df_dy__(xx_old, yy_old)
    f_value_new = __function__(xx_new, yy_new)

    if abs(f_value_new - f_value_old) < get_eps():
      break
  return ans_list

start()
