import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from .functions import choise_function


# Функция для инициализации популяции
def initialize_population(pop_size, x_min, x_max, y_min, y_max,x_step, y_step):
    x = np.arange(x_min, x_max, x_step)
    y = np.arange(y_min, y_max, y_step)
    x_samples, y_samples = np.meshgrid(x, y)
    population = np.column_stack((x_samples.ravel(), y_samples.ravel()))
    if pop_size < population.shape[0]:
        population = population[np.random.choice(population.shape[0], pop_size, replace=False)]
    return population


# Функция для вычисления пригодности (фитнеса) особей
def fitness(population, fitness_function):
    x = population[:, 0]
    y = population[:, 1]
    return 1/ (fitness_function(x, y) + 1e-6)



def select_parents(population, fitness_values, tournament_size=2):
    selected_parents = []
    population_size = population.shape[0]
    num_parents = population_size//2
    if num_parents%2 != 0: num_parents +=1
    print (num_parents)

    # Случайно перемешиваем исходную популяцию
    np.random.shuffle(population)
    print("start population")
    print (population)
    
    while len(selected_parents) < num_parents:

        # Проверяем, если количество особей четное
        if len(population) % 2 == 0:
            # Разбиваем популяцию на группы по две особи
            groups = np.array_split(population, len(population) // 2)
        elif(len(population)>3):
            # Разбиваем популяцию на группы по две особи, кроме последних трех
            groups = np.array_split(population[:-3], (len(population) - 3) // 2)

            # Создаем отдельную группу с последними тремя особями
            last_group = population[-3:]

            # Добавляем последний турнир из трех особей
            groups.append(last_group)
        else:
            last_group = population[-3:]
            groups.append(last_group)

        print(groups)
        for group in groups:
            group_indices = np.arange(len(group))  # Создать массив индексов особей в группе
            group_fitness = fitness_values[group_indices]  # Вычислить приспособленность для группы
            winner_index = group[group_indices[np.argmax(group_fitness)]]  # Выбрать наиболее приспособленную особь
            
            selected_parents.append(winner_index)
            
            # Удаляем выбранную особь из группы
            population = np.delete(population, np.where((population == winner_index).all(axis=1)), axis=0)

            # Если промежуточная популяция достигла нужного размера, выходим из цикла
            if len(selected_parents) == num_parents:
                break
        print("bad parents")
        print (population)

    return np.array(selected_parents), np.array(population)


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



def mutate(children, mutation_rate=0.01):
    mutation_mask = np.random.rand(*children.shape) < mutation_rate
    children[mutation_mask] += np.random.rand(*children.shape)[mutation_mask]
    return children


# Главная функция генетического алгоритма
def genetic_algorithm(pop_size, generations, fitness_function,x_min, x_max, y_min, y_max,x_step,y_step):
    best_individual_history = []  # Список для отслеживания лучшей особи на каждом поколении
    all_generations = []  # Список для отслеживания всех поколений

    #Генерим популяцию
    population = initialize_population(pop_size,x_min, x_max, y_min, y_max,x_step,y_step)
    best_individual = None

    for generation in range(generations):
        #К популяции применяем фитнес-функцию(вычисляем приспособленность каждой особи)
        fitness_values = fitness(population, fitness_function)
        print (fitness_values)

        # Добавили данные для вывода
        best_index = np.argmax(fitness_values)  # Индекс лучшей особи
        best_individual = population[best_index]  # Лучшая особь на данном поколении



        best_individual_as_list = best_individual.tolist()  # Преобразуем массив в список
        best_individual_history.append(best_individual_as_list)  # Сохраняем лучшую особь
        all_generations.append(population.tolist())  # Сохраняем все особи текущего поколения

        #Выбираем родителей для скрещивания из популяции
        parents,bad_parents = select_parents(population, fitness_values)

        children = crossover(parents)
        children = mutate(children)
        population = np.concatenate((children, bad_parents), axis=0)
        print ("pop")
        print(len(population))
        print("val pop")
        print(population)
    print("best_individual_history")
    print(best_individual_history)
    best_overall_individual = min(best_individual_history, key=lambda x: max(x))
    best_individual = best_overall_individual
    return best_individual, best_individual_history, all_generations 
