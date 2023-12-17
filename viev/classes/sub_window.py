import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget,QVBoxLayout, QDialog, QVBoxLayout
from PyQt5.uic import loadUi
from .add_graphic import create_3d_plot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class SubWindow(QMainWindow):
    def __init__(self, ui_filename, main_window):
        super().__init__()
        self.initUI(ui_filename)
        self.main_window = main_window  # Сохраняем ссылку на главное окно

    def initUI(self, ui_filename):
        loadUi(ui_filename, self)

    def closeEvent(self, event):
        # Сохраняем позицию и геометрию SubWindow перед закрытием
        self.main_window.last_sub_window_position = self.pos()
        self.main_window.last_sub_window_geometry = self.geometry()
        self.main_window.show()  # При закрытии дополнительного окна, показываем главное окно

    def button_click_handler(self,func,all_generations,x_min, x_max, y_min, y_max,x_step, y_step):

        create_3d_plot(func,all_generations,x_min, x_max, y_min, y_max,x_step, y_step)