from .sub_window import SubWindow
from PyQt5.QtWidgets import QPushButton, QMessageBox
from modules.genetic import *
class SubWindowGeneticAlgorithm(SubWindow):
    def __init__(self, main_window, window_name):
        ui_filename = f'viev/windows/subwindow_{window_name}.ui'
        super().__init__(ui_filename, main_window)
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.button_click_handler)
    
    def button_click_handler(self):
        # Обработчик события для нажатия кнопки
        # Вывести сообщение в консоль
        # Запуск генетического алгоритма
        genetic_algorithm(pop_size=100, genome_length=3, generations=100)

        print("Глеб пидр")

        # Вывести сообщение в диалоговом окне
        QMessageBox.information(self, "Глеб пидр", "Глеб пидр")
