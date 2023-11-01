import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QPushButton, QLineEdit
from PyQt5.QtChart import QChartView, QChart
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtGui import QFont  # Добавьте импорт QFont
from modules.genetic import *
from matplotlib import cm

def rosenbrock(x, y, z):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2 + z ** 2

def himmelblau(x, y, z):
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - 7) ** 2 + z ** 2

class MatplotlibWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.canvas = FigureCanvas(plt.figure())

        layout.addWidget(self.canvas)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("3D Plot Example")

        container = QWidget(self)
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        input_layout = QVBoxLayout()

        self.param_x = QLineEdit("0", self)
        self.param_x.setMaximumSize(100, 20)
        self.param_y = QLineEdit("0", self)
        self.param_y.setMaximumSize(100, 20)
        self.param_z = QLineEdit("0", self)
        self.param_z.setMaximumSize(100, 20)
        self.combo_box_function = QComboBox(self)
        self.combo_box_function.setMaximumSize(200, 20)
        self.combo_box_function.addItem("Функция Розенброка")
        self.combo_box_function.addItem("Функция Химмельблау")

        self.combo_box_algorithm = QComboBox(self)
        self.combo_box_algorithm.setMaximumSize(200, 20)
        self.combo_box_algorithm.addItem("Градиентный спуск")
        self.combo_box_algorithm.addItem("Кун Таккер")
        self.combo_box_algorithm.addItem("Генетический")
        self.combo_box_algorithm.addItem("Роя частиц")
        self.combo_box_algorithm.addItem("Пчелиного роя")
        self.combo_box_algorithm.addItem("Искуственной иммунной системмы")
        self.combo_box_algorithm.addItem("Бактериальной оптимизации")
        self.combo_box_algorithm.addItem("Гибридный")

        font = QFont()
        font.setPointSize(12)
        self.param_x.setFont(font)
        self.param_y.setFont(font)
        self.param_z.setFont(font)
        self.combo_box_function.setFont(font)
        self.combo_box_algorithm.setFont(font)

        input_layout.addWidget(self.param_x)
        input_layout.addWidget(self.param_y)
        input_layout.addWidget(self.param_z)
        input_layout.addWidget(self.combo_box_function)
        input_layout.addWidget(self.combo_box_algorithm)

        layout.addLayout(input_layout)

        # Центральная область - график с результатом


        # Нижний ряд - кнопка для обработки данных
        button = QPushButton("Обработать данные", self)
        layout.addWidget(button)

        # Обработчик нажатия кнопки
        button.clicked.connect(self.process_data)

        # Используйте MatplotlibWidget для отображения графика
        self.matplotlib_widget = MatplotlibWidget()
        layout.addWidget(self.matplotlib_widget)
        self.matplotlib_widget.setMinimumSize(800, 600)


    def process_data(self):
        selected_function = self.combo_box_function.currentText()
        selected_algorithm = self.combo_box_algorithm.currentText()
        x = float(self.param_x.text())
        y = float(self.param_y.text())
        z = float(self.param_z.text())

        if selected_algorithm == "Генетический":
            # Вызов генетического алгоритма
            best_individual, best_individual_history, all_generations = genetic_algorithm(pop_size=100, genome_length=3, generations=100)
            result = best_individual_history  # Здесь предполагается, что fitness_history содержит результаты
            print(len(result))
            # Отобразить результат в MatplotlibWidget с использованием matplotlib
            fig = self.matplotlib_widget.canvas.figure
            fig.clf()
            ax = fig.add_subplot(111, projection='3d')
            for coordinates in result:
                x, y, z = coordinates
                ax.scatter(x, y, z, c='r', marker='o')
            x,y,z = best_individual
            ax.scatter(x, y, z, c='b', marker='o',label="best_individual")
            ax.set_xlabel('Поколение')
            ax.set_ylabel('Пригодность')
            ax.set_zlabel('Z')
            X = np.linspace(-2, 2, 100)
            Y = np.linspace(-2, 2, 100)
            X, Y = np.meshgrid(X, Y)
            Z = rosenbrock(X, Y, 0)  # Функция Розенброка без учета Z (задайте 0)

            # Построение поверхности функции Розенброка
            ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, alpha=0.5)

        else:
            # Вычислите результат для выбранной функции
            if selected_function == "Функция Розенброка":
                result = rosenbrock(x, y, z)
            elif selected_function == "Функция Химмельблау":
                result = himmelblau(x, y, z)

            # Отобразить результат в MatplotlibWidget с использованием matplotlib
            fig = self.matplotlib_widget.canvas.figure
            fig.clf()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(0, 0, 0, c='r', marker='o', label=f'Result: {result}')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            plt.legend()

        self.matplotlib_widget.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
