from .genetic import *
from .imun import *


def getHistoryBestPoint(population, func):
    history_best_points = []
    for i in range(len(population)):
        history_best_points.append((population[i][0], population[i][1], func(population[i][0], population[i][1])))
    return history_best_points



def gibrid(x_min, x_max, x_step, y_min,y_max, y_step,population_size, num_generations, lambda_func):
    # Создаём общую популяцию
    #_i
    population = create_population(x_min, x_max, y_min, y_max, population_size)
    list_of_population = []
    history_best_points = []
    best_point = [population[0][0], population[0][1], lambda_func(population[0][0], population[0][1])]

    for i in range(num_generations):
        gen_pop = genetic_algorithm(population)
        imun_pop = algorithm_artificial_immune_system(gen_pop, population_size, lambda_func, 2)

        list_of_population.append(population)
        # Заменяем старую популяцию новой
        population = imun_pop
        sort_pop = sorted(population, key=lambda x: lambda_func(x[0], x[1]))
        fitnessFunc = getHistoryBestPoint(sort_pop, lambda_func)
        history_best_points.append(fitnessFunc[0:5])

        if best_point[2] > lambda_func(sort_pop[0][0], sort_pop[0][1]):
            best_point = [sort_pop[0][0], sort_pop[0][1], lambda_func(sort_pop[0][0], sort_pop[0][1])]

    return list_of_population

