import random
from sympy import *


def __get_function__(lambda_func):
  x, y = symbols('x y')
  return lambda_func(x, y)


def __df_dx__(lambda_func, x, y):
  add_func = __get_function__(lambda_func)
  xs, ys = symbols('x y')
  df_dx = diff(add_func, xs)
  return df_dx.subs([(xs, x), (ys, y)])


def __df_dy__(lambda_func, x, y):
  add_func = __get_function__(lambda_func)
  xs, ys = symbols('x y')
  df_dy = diff(add_func, ys)
  return df_dy.subs([(xs, x), (ys, y)])


def __generate_random_float__(start, end, step):
  num_values = int((end - start) / step) + 1
  random_value = random.randint(0, num_values - 1)
  result = start + random_value * step

  return result


def method_performs_iterative_optimization_using_the_function_in_3D_visualizing_the_process(x_min, x_max, x_step, y_min,
                                                                                            y_max, y_step, get_lmd,
                                                                                            get_eps, get_n,
                                                                                            lambda_func):
  xx_new = __generate_random_float__(x_min, x_max, x_step)
  yy_new = __generate_random_float__(y_min, y_max, y_step)
  f_value_new = lambda_func(xx_new, yy_new)
  ans_list = []

  for n in range(get_n):
    xx_old = xx_new
    yy_old = yy_new
    f_value_old = f_value_new

    ans_list.append([xx_old, yy_old])

    xx_new = xx_old - get_lmd * __df_dx__(lambda_func, xx_old, yy_old)
    yy_new = yy_old - get_lmd * __df_dy__(lambda_func, xx_old, yy_old)
    f_value_new = lambda_func(xx_new, yy_new)

    if abs(f_value_new - f_value_old) < get_eps or xx_new < x_min or xx_new > x_max or yy_new < y_min or yy_new > y_max:
      break
  print(ans_list)
  return ans_list