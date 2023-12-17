import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Функция Розенброка
def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

# Шаг 1: Генерация случайных точек
def generate_random_points(space_size, So):
    points = [(random.uniform(-space_size, space_size), random.uniform(-space_size, space_size)) for _ in range(So)]
    return points

# Шаг 2: Выделение элитных и перспективных участков
def select_elite_and_promising(points, Ab, Ap):
    sorted_points = sorted(points, key=lambda point: rosenbrock(*point))
    elite_centers = sorted_points[:Ab]
    promising_centers = sorted_points[:Ab + Ap]
    return elite_centers, promising_centers

# Шаг 3: Вычисление значений целевой функции для всех точек
def compute_fitness_for_all(points):
    fitness_values = [rosenbrock(*point) for point in points]
    return fitness_values

# Основной алгоритм с визуализацией и задержкой
def main_algorithm(space_size, So, Ab, Ap, nb, np, Sw, max_iterations):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    iteration = 0
    best_point = None
    while not check_termination_conditions(iteration, max_iterations):
        points = generate_random_points(space_size, So)
        fitness_values = compute_fitness_for_all(points)
        elite_centers, promising_centers = select_elite_and_promising(points, Ab, Ap)

        iteration += 1

    # Отображаем лучшую точку красным цветом
    best_x, best_y = best_point
    best_z = rosenbrock(best_x, best_y)
    ax.scatter(best_x, best_y, best_z, c='r', marker='x', label='Best Point',s=1000)

    # Выводим лучшую точку
    print("Лучшая точка:", best_point)

    plt.show()

# Шаг 4: Проверка условий завершения итерации
def check_termination_conditions(iteration, max_iterations):
    return iteration >= max_iterations

# Пример использования
space_size = 5
So = 100
Ab = 10
Ap = 20
nb = 5
np = 15
Sw = 1000
max_iterations = 2
main_algorithm(space_size, So, Ab, Ap, nb, np, Sw, max_iterations)
