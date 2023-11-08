import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtChart import QChartView, QChart
from PyQt5.QtGui import QFont
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib import cm  # Импортируйте модуль colormap
# Функция для создания 3D графика
def create_3d_plot(result, func,all_generations, x_min, x_max, y_min, y_max, x_step, y_step):

    X = np.arange(x_min, x_max, x_step)
    Y = np.arange(y_min, y_max, y_step)
    X, Y = np.meshgrid(X, Y)
    Z = func(X, Y)  # Вычислите значения функции Z в зависимости от X и Y

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.5)


    generation_counter = 0
    scatter_points = []  # Список для отслеживания объектов Scatter

    for generation in all_generations:
        # Удалите предыдущие объекты Scatter
        for scatter in scatter_points:
            scatter.remove()
        scatter_points.clear()

        for coordinates in generation:
            x, y = coordinates
            z = func(x, y)
            scatter = ax.scatter(x, y, z, c='r', marker='o')
            scatter_points.append(scatter)

            x1, y1 = result[generation_counter]
            z1 = func(x1, y1)
            scatter_result = ax.scatter(x1, y1, z1, c='g', marker='o')
            scatter_points.append(scatter_result)

        plt.pause(0.2)

    # x, y = best_individual
    # # Здесь z соответствует значению функции Z в этой точке
    # z = func(x, y)
    # ax.scatter(x, y, z, c='g', marker='o')


    # for coordinates in result:
    #     plt.pause(0.0001)
    #     x, y = coordinates
    #     # Здесь z соответствует значению функции Z в этой точке
    #     z = func(x, y)
    #     ax.scatter(x, y, z, c='r', marker='o')