from .genetic_algorithm import SubWindowGeneticAlgorithm
from .gradient_descent import SubWindowGradientDescent
from .kun_takker import SubWindowKunTakker
from .particle_swarm import SubWindowParticleSwarm
from .bee_swarm import SubWindowBeeSwarm
from .artifitial_immune_network import SubWindowArtifitialImmuneNetwork
from .bakterial_optimization import SubWindowBakterialOptimization
from .sub_window import SubWindow
from .dimensional_algorithm import SubWindowDimensionalAlgorithm
import importlib

from modules.camel_case import camel_case

class SubWindowFactory:
    
    def create_sub_window(window_name, main_window):
        try:
            print(window_name)
            sub_window_module = importlib.import_module(f".{window_name}", package="viev.classes")

            window_class = camel_case(window_name)
            sub_window_class = getattr(sub_window_module, f"SubWindow{window_class}")
            return sub_window_class(main_window, window_name)
        except ImportError:
            raise ValueError(f"Не удалось импортировать модуль для подокна: {window_name}")
        except AttributeError:
            raise ValueError(f"Не найден класс для подокна: SubWindow{window_name.capitalize()}")

