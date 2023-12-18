from .sub_window import SubWindow
from PyQt5.QtWidgets import QPushButton, QMessageBox, QLineEdit,QComboBox
from modules.particle_swarm import *
from modules.functions import choise_function

class SubWindowParticleSwarm(SubWindow):
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
            'size_swarm':self.findChild(QLineEdit,'size_swarm'),
            'currentVelocityRatio':self.findChild(QLineEdit,'currentVelocityRatio'),
            'localVelocityRatio':self.findChild(QLineEdit,'localVelocityRatio'),
            'globalVelocityRatio':self.findChild(QLineEdit,'globalVelocityRatio'),
            'numbersOfLife':self.findChild(QLineEdit,'numbersOfLife'),

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
        size_swarm = int(self.line_edits['size_swarm'].text())
        currentVelocityRatio = float(self.line_edits['currentVelocityRatio'].text())
        localVelocityRatio = float(self.line_edits['localVelocityRatio'].text())
        globalVelocityRatio = float(self.line_edits['globalVelocityRatio'].text())
        numbersOfLife = int(self.line_edits['numbersOfLife'].text())



        selected_item = self.combo_box.currentText()
        func_name = selected_item
        self.func = choise_function(func_name)
        ff = self.func
        swarm = Swarm(x_min, x_max, x_step, y_min,y_max, y_step,size_swarm,currentVelocityRatio,localVelocityRatio,globalVelocityRatio
            ,numbersOfLife,ff,-10,10)

        history= swarm.startSwarm()
        # Вызов суперклассового обработчика с передачей result и func
        super().button_click_handler(self.func,history,x_min, x_max, y_min, y_max,x_step, y_step)



# # Запускаем алгоритм оптимизации
# result = swarm.startSwarm()
# print(result)