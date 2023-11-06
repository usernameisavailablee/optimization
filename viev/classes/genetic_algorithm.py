from .sub_window import SubWindow
from PyQt5.QtWidgets import QPushButton, QMessageBox, QLineEdit,QComboBox
from modules.genetic import *
from modules.functions import choise_function
class SubWindowGeneticAlgorithm(SubWindow):
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
            'pop_size':self.findChild(QLineEdit,'pop_size'),
            'generations':self.findChild(QLineEdit,'generations')
        }


        self.result = [[0,0]]
        self.func = None

        self.button.clicked.connect(self.button_click_handler)
        
    def button_click_handler(self):
        # x_min = float(x_min.text())
        # x_max = float(x_max.text())
        # y_min = float(y_min.text())
        # y_max = float(y_max.text())
        # x_step = float(x_step.text())
        # y_step = float(y_step.text())

        x_min = float(self.line_edits['x_min'].text())
        x_max = float(self.line_edits['x_max'].text())
        y_min = float(self.line_edits['y_min'].text())
        y_max = float(self.line_edits['y_max'].text())
        x_step = float(self.line_edits['x_step'].text())
        y_step = float(self.line_edits['y_step'].text())
        pop_size = int(self.line_edits['pop_size'].text())
        generations = int(self.line_edits['generations'].text())


        selected_item = self.combo_box.currentText()
        func_name = selected_item
        self.func = choise_function(func_name)
    #    best_individual, best_individual_history,all_generations  = genetic_algorithm(pop_size=100, genome_length=3, generations=10,self.func)
        ff = self.func
        best_individual, best_individual_history, all_generations = genetic_algorithm(pop_size, generations,self.func,x_min, x_max, y_min, y_max,x_step, y_step)
        self.result = best_individual_history
        # Вызов суперклассового обработчика с передачей result и func
        super().button_click_handler(self.result, self.func,best_individual,x_min, x_max, y_min, y_max,x_step, y_step)




#        self.comboBox = self.findChild(QComboBox, 'comboBox_Function')
#        self.comboBox.currentIndexChanged.connect(self.function_selection_changed)


#selected_function = self.comboBox.currentText()


