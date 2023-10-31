import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.uic import loadUi
from .sub_window_factory import SubWindowFactory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.current_sub_window = None
        self.last_sub_window_position = None  # Добавляем атрибут для сохранения позиции последнего подокна
        self.last_sub_window_geometry = None  # Добавляем атрибут для сохранения геометрии последнего подокна
        self.setGeometry(100, 100, 800, 600)

    def initUI(self):

        loadUi('windows/main.ui', self)

        for button in self.findChildren(QPushButton):
            if button.objectName().startswith("btn"):
                button.clicked.connect(self.openWindow)

    def openWindow(self):
        if self.current_sub_window:
            self.current_sub_window.close()

        if self.last_sub_window_position and self.last_sub_window_geometry:
            self.setGeometry(self.last_sub_window_geometry)  # Восстанавливаем геометрию главного окна
            self.move(self.last_sub_window_position)  # Устанавливаем позицию главного окна
            self.last_sub_window_position = None  # Сбрасываем позицию

        self.hide()
        sender_button = self.sender()
        window_name = sender_button.objectName()
        window_name = window_name[4:]
        sub_window = SubWindowFactory.create_sub_window(window_name, self)
        self.current_sub_window = sub_window
        sub_window.show()
