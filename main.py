import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.uic import loadUi
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
from viev.classes.sub_window_factory import SubWindowFactory
from viev.classes.main_window import MainWindow
from viev.classes.gradient_decent import SubWindowGradientDescent
from viev.classes.genetic_algorithm import SubWindowGeneticAlgorithm
from viev.classes.sub_window import SubWindow
from modules.camel_case import camel_case


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())