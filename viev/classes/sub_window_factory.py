
from genetic_algorithm import SubWindowGeneticAlgorithm
from gradient_descent import SubWindowGradientDescent
from sub_window import SubWindow
import importlib

from modules.camel_case import camel_case

class SubWindowFactory:
    
    def create_sub_window(window_name, main_window):
        try:
            print(window_name)
            sub_window_module = importlib.import_module(window_name)
            window_class = camel_case(window_name)
            sub_window_class = getattr(sub_window_module, f"SubWindow{window_class}")
            return sub_window_class(main_window, window_name)
        except ImportError:
            raise ValueError(f"Не удалось импортировать модуль для подокна: {window_name}")
        except AttributeError:
            raise ValueError(f"Не найден класс для подокна: SubWindow{window_name.capitalize()}")

