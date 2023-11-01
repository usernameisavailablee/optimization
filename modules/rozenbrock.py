import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определение функции Розенброкка для трех переменных
def rosenbrock(x, y, z):
    return (1 - x)**2 + 100 * (y - x**2)**2 + z**2

# Функция для инициализации популяции
def initialize_population(pop_size, genome_length):
    return np.random.rand(pop_size, genome_length)

# Функция для вычисления пригодности (фитнеса) особей
def fitness(population):
    x = population[:, 0]
    y = population[:, 1]
    z = population[:, 2]
    return 1 / (rosenbrock(x, y, z) + 1e-6)

# Функция для выбора родителей на основе рулеточной селекции
def select_parents(population, fitness_values):
    normalized_fitness = fitness_values / np.sum(fitness_values)
    parent_indices = np.random.choice(len(population), size=len(population), p=normalized_fitness)
    return population[parent_indices]

# Функция для скрещивания (кроссовера) родителей
def crossover(parents, crossover_rate=0.7):
    children = np.empty_like(parents)
    for i in range(0, len(parents), 2):
        if np.random.rand() < crossover_rate:
            crossover_point = np.random.randint(1, len(parents[i]))
            children[i] = np.concatenate((parents[i][:crossover_point], parents[i + 1][crossover_point:]))
            children[i + 1] = np.concatenate((parents[i + 1][:crossover_point], parents[i][crossover_point:]))
        else:
            children[i] = parents[i]
            children[i + 1] = parents[i + 1]
    return children

# Функция для мутации
def mutate(children, mutation_rate=0.01):
    mutation_mask = np.random.rand(*children.shape) < mutation_rate
    children[mutation_mask] = np.random.rand(np.sum(mutation_mask))
    return children

# Главная функция генетического алгоритма
# Главная функция генетического алгоритма
def genetic_algorithm(pop_size, genome_length, generations):
    fitness_history = []  # Список для отслеживания лучшей пригодности на каждом поколении
    population = initialize_population(pop_size, genome_length)
    for generation in range(generations):
        fitness_values = fitness(population)
        parents = select_parents(population, fitness_values)
        children = crossover(parents)
        children = mutate(children)
        population = children
        best_fitness = np.max(fitness_values)
        best_individual = population[np.argmax(fitness_values)]
        fitness_history.append(best_fitness)
        print(f"Поколение {generation}: Лучшая пригодность = {best_fitness}, Лучший индивид = {best_individual}")

    # Создание 3D-графика для отображения функции Розенброкка
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-2, 2, 100)
    y = np.linspace(-1, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = rosenbrock(X, Y, 0)  # Фиксируйте z на нуле, так как функция трех переменных
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Функция Розенброкка в трехмерном пространстве')

    # Добавление точек, представляющих популяцию на графике
    best_x = best_individual[0]
    best_y = best_individual[1]
    best_z = 0  # Здесь также фиксируйте z на нуле
    best_w = rosenbrock(best_x, best_y, best_z)
    ax.scatter([best_x], [best_y], [best_w], color='red', s=50, label='Лучший индивид')
    plt.legend()
    plt.show()

