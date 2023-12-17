from .sub_window import SubWindow
from PyQt5.QtWidgets import QPushButton, QMessageBox, QLineEdit,QComboBox
from modules.lab2 import *
from modules.functions import choise_function

class SubWindowKunTakker(SubWindow):
    def __init__(self, main_window, window_name):
        ui_filename = f'viev/windows/subwindow_{window_name}.ui'
        super().__init__(ui_filename, main_window)
        self.button = self.findChild(QPushButton, 'pushButton')
        self.combo_box = self.findChild(QComboBox, 'comboBox_Function')

        self.line_edits = {
            'x_min': self.findChild(QLineEdit, 'x_min'),
            'x_max': self.findChild(QLineEdit, 'x_max'),
            'y_min': self.findChild(QLineEdit, 'y_min'),
            'y_max': self.findChild(QLineEdit, 'y_max'),
            'x_step': self.findChild(QLineEdit, 'x_step'),
            'y_step': self.findChild(QLineEdit, 'y_step'),
            'len_side':self.findChild(QLineEdit,'len_side'),

        }


        self.result = [[0,0]]
        self.func = None

        self.button.clicked.connect(self.button_click_handler)

    def button_click_handler(self):

        x_min = float(self.line_edits['x_min'].text())
        x_max = float(self.line_edits['x_max'].text())
        y_min = float(self.line_edits['y_min'].text())
        y_max = float(self.line_edits['y_max'].text())
        x_step = float(self.line_edits['x_step'].text())
        y_step = float(self.line_edits['y_step'].text())
        len_side = float(self.line_edits['len_side'].text())



        selected_item = self.combo_box.currentText()
        func_name = selected_item
        self.func = choise_function(func_name)
        ff = self.func

        history= method_splain_fly(x_min, x_max, x_step, y_min,y_max, y_step,len_side,ff)
        # Вызов суперклассового обработчика с передачей result и func
        super().button_click_handler(self.func,history,x_min, x_max, y_min, y_max,x_step, y_step)