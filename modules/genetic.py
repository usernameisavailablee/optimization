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
    best_individual_history = []  # Список для отслеживания лучшей особи на каждом поколении
    all_generations = []  # Список для отслеживания всех поколений
    population = initialize_population(pop_size, genome_length)
    best_individual = None

    for generation in range(generations):
        fitness_values = fitness(population)
        best_index = np.argmax(fitness_values)  # Индекс лучшей особи
        best_individual = population[best_index]  # Лучшая особь на данном поколении
        best_individual_as_list = best_individual.tolist()  # Преобразуем массив в список
        best_individual_history.append(best_individual_as_list)  # Сохраняем лучшую особь
        all_generations.append(population.tolist())  # Сохраняем все особи текущего поколения
        parents = select_parents(population, fitness_values)
        children = crossover(parents)
        children = mutate(children)
        population = children

    return best_individual, best_individual_history, all_generations 


# best_individual, best_individual_history,all_generations  = genetic_algorithm(pop_size=100, genome_length=3, generations=10)
# print(all_generations)
