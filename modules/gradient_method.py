from datetime import time
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D
matplotlib.use('TkAgg')  # or 'Qt5Agg'


# получить шаг сходимости
def get_lmd1():
  return 0.00001


def get_lmd2():
  return 0.00001


# получить число итераций
def get_n():
  return 10


# получить начальное значение
def get_x0y0():
  return [0, 0]


def rosenbrock(x, y):
  return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


def drosenbrock_dx(x, y):
  return -2 * (1 - x) - 400 * x * (y - x ** 2)


def drosenbrock_dy(x, y):
  return 200 * (y - x ** 2)


def start():
  x_plt = np.arange(0, 5, 0.2)
  y_plt = np.arange(0, 5, 0.2)
  rosenbrock_plt = np.array([[rosenbrock(x, y) for x in x_plt] for y in y_plt])

  plt.ion()  # включение интерактивного режима отображения графиков

  fig = plt.figure()
  ax = Axes3D(fig)

  x, y = np.meshgrid(x_plt, y_plt)
  ax.plot_surface(x, y, rosenbrock_plt, color='y', alpha=0.5)

  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('rosenbrock')

  xx, yy = get_x0y0()

  point = ax.scatter(xx, yy, rosenbrock(xx, yy),
                     c='red')  # отображение точки красным цветом

  for n in range(get_n()):
    xx = xx - get_lmd1() * drosenbrock_dx(xx, yy)
    yy = yy - get_lmd2() * drosenbrock_dy(xx, yy)

    ax.scatter(xx, yy, rosenbrock(xx, yy), c='red')

    # перерисовка графика и задержка на 10 мс
    fig.canvas.draw()
    fig.canvas.flush_events()

    time.sleep(0.1)
    plt.show()

    print(xx, yy)

  plt.ioff()  # выключение интерактивного режима отображения графиков
  plt.show()

start()