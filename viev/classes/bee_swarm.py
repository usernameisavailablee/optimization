from .sub_window import SubWindow
from PyQt5.QtWidgets import QPushButton, QMessageBox

class SubWindowBeeSwarm(SubWindow):
    def __init__(self, main_window, window_name):
        ui_filename = f'viev/windows/subwindow_{window_name}.ui'
        super().__init__(ui_filename, main_window)
