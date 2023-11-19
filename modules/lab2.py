import random
import time


import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
matplotlib.use('TkAgg')  # or 'Qt5Agg'


def __generate_random_float__(start, end, step):
  num_values = int((end - start) / step) + 1
  random_value = random.randint(0, num_values - 1)
  result = start + random_value * step
  return result


def mean(list):
  assert len(list) != 0
  sum_of_x = 0
  sum_of_y = 0
  for xy in list:
    sum_of_x += xy[0]
    sum_of_y += xy[1]
  return sum_of_x, sum_of_y


def calc_new_point(list_without_worst_element, worst_element):
  x, y = mean(list_without_worst_element)
  return (x - worst_element[0], y - worst_element[1])


def iteration(list_start, lambda_func):
  func_min = max(list_start, key=lambda x: lambda_func(x[0], x[1]))
  list_without_worst_element = list(filter(lambda x: x != func_min, list_start))
  new_point = calc_new_point(list_without_worst_element, func_min)
  list_without_worst_element.append(new_point)
  return list_without_worst_element


def find_best_min_value(list_of_element, lambda_func):
  func_min = min(list_of_element, key=lambda x: lambda_func(x[0], x[1]))
  return lambda_func(func_min[0], func_min[1])


def method_splain_fly(x_min, x_max, x_step, y_min, y_max, y_step, get_length, lambda_func):
  assert x_max - x_min > get_length and y_max - y_min > get_length, "Длина задана больше обласьти опреления"



  x0 = __generate_random_float__(x_min + get_length, x_max, x_step)
  y0 = __generate_random_float__(y_min, y_max - get_length, y_step)
  x1 = x0 - get_length
  y1 = y0
  x2 = x0 - get_length / 2
  y2 = y0 + get_length

  list_of_points = [(x0, y0), (x1, y1), (x2, y2)]
  new_min_value = find_best_min_value(list_of_points, lambda_func)
  best_min_value = new_min_value
  flag_best_twice = 0

  while True:

    list_of_points = iteration(list_of_points, lambda_func)
    new_min_value = find_best_min_value(list_of_points, lambda_func)

    print(best_min_value)

    if best_min_value == new_min_value:
      flag_best_twice += 1
      if flag_best_twice == 3:
        break
    elif best_min_value > new_min_value:
      flag_best_twice = 0
      best_min_value = new_min_value

  return list_of_points


method_splain_fly(-5, 5, 0.5, -5, 5, 0.5, 0.1, lambda x, y: (1 - x) ** 2 + 100 * (y - x ** 2) ** 2)
