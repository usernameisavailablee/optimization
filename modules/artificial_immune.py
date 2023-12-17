import random


def algorithm_artificial_immune_system(min_x, max_x, x_step, min_y, max_y, y_step, population_size, generations,
                                       lambda_func):
  # Задайте параметры алгоритма
  mutation_rate = 0.1
  # Список лучших точек в каждой популяции
  history_best_point = []

  # Инициализация популяции антител
  # _i
  population = [(random.uniform(min_x, max_x), random.uniform(min_y, max_y)) for _ in range(population_size)]
  list_of_population = []
  # Основной цикл оптимизации
  for generation in range(generations):
    list_of_population.append(population)
    # Оценка функции аффинности для каждого антитела
    fitness_values = [lambda_func(x, y) for x, y in population]

    # Отбор антител
    selected_population = []
    for _ in range(population_size):
      selected_index = random.choices(range(population_size), weights=[1 / v for v in fitness_values], k=1)[0]
      selected_population.append(population[selected_index])

    # Мутация
    for i in range(population_size):
      if random.random() < mutation_rate:
        x, y = selected_population[i]
        x += random.uniform(-0.1, 0.1)
        y += random.uniform(-0.1, 0.1)
        selected_population[i] = (x, y)
    # Запишем лучшую точку в данной популяции и её решение
    best_solution = min(population, key=lambda ind: lambda_func(ind[0], ind[1]))
    history_best_point.append((best_solution[0], best_solution[1], (lambda_func(best_solution[0], best_solution[1]))))
    # Замена старой популяции новой
    population = selected_population

  # Вывод лучшего решения
  best_solution = min(population, key=lambda ind: lambda_func(ind[0], ind[1]))

  return list_of_population
