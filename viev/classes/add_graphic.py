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
def create_3d_plot(result, func):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for coordinates in result:
        x, y = coordinates
        ax.scatter(x, y, c='r', marker='o')
    
    # Постройте поверхность
    X = np.linspace(-2, 2, 100)
    Y = np.linspace(-2, 2, 100)
    X, Y = np.meshgrid(X, Y)
    Z = func(X, Y)  # Вызовите функцию с аргументами X и Y

    ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.5)

    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('ыыы')
    
    return fig

# # Создание приложения PyQt
# app = QApplication(sys.argv)
# window = QMainWindow()
# window.setGeometry(100, 100, 800, 600)
# central_widget = QWidget()
# layout = QVBoxLayout(central_widget)
# window.setCentralWidget(central_widget)

# # Пример вызова функции
# # Результаты точек (замените на свои данные)
# result = [(1, 1, 1), (2, 2, 2), (3, 3, 3)]
# # Функция, которая вычисляет Z (замените на вашу функцию)
# def func(x, y):
#     return np.sin(np.sqrt(x**2 + y**2))

# fig = create_3d_plot(result, func)

# canvas = FigureCanvas(fig)
# layout.addWidget(canvas)

# window.show()
# sys.exit(app.exec_())
