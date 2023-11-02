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


        self.result = [[0,0]]
        self.func = None

        self.button.clicked.connect(self.button_click_handler)
        
    def button_click_handler(self):
        selected_item = self.combo_box.currentText()
        func_name = selected_item
        self.func = choise_function(func_name)
    #    best_individual, best_individual_history,all_generations  = genetic_algorithm(pop_size=100, genome_length=3, generations=10,self.func)
        ff = self.func
        best_individual, best_individual_history, all_generations = genetic_algorithm(100, 3, 100,self.func,0,20,0,20,0.001,0.001)
        print(best_individual_history)
        self.result = best_individual_history
        # Вызов суперклассового обработчика с передачей result и func
        super().button_click_handler(self.result, self.func)




#        self.comboBox = self.findChild(QComboBox, 'comboBox_Function')
#        self.comboBox.currentIndexChanged.connect(self.function_selection_changed)


#selected_function = self.comboBox.currentText()


