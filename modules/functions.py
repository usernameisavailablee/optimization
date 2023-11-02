import numpy as np


# для импорта функций: from modules.functions import *
def choise_function(function_name):
  if function_name == "Функция Розенброкка":
    return lambda x, y: (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

  elif function_name == "Функция Химмельблау":
    return lambda x, y: (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2

  elif function_name == "Функция Экли":
    return lambda x, y: -(y + 47) * np.sin(np.sqrt(np.abs(x / 2 + (y + 47)))) - x * np.sin(
      np.sqrt(np.abs(x - (y + 47))))

  elif function_name == "Функция Изома":
    return lambda x, y: -20 * np.exp(-0.2 * np.sqrt(0.5 * (x ** 2 + y ** 2))) - np.exp(
      0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.exp(1) + 20

  elif function_name == "Функция Хольдера":
    return lambda x, y: -np.abs(np.sin(x) * np.cos(y) * np.exp(np.abs(1 - np.sqrt(x ** 2 + y ** 2) / np.pi)))
