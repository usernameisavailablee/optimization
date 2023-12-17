import random


# Разделим пчёл на группы
def divide_bees_by_group(number_group_best, number_group_perspective, valeu):
    a = round((valeu / 100 * 70) / number_group_best, 0)
    b = round((valeu - a * number_group_best) / number_group_perspective, 0)
    return int(a), int(b)


# Гененрация новой точки в области старой с заданным диапазоном и границами
def create_new_point(min_x, max_x, now_x, spread_points):
    rand_x = round(random.uniform(now_x - spread_points, now_x + spread_points), 3)
    while rand_x < min_x or rand_x > max_x:
        rand_x = round(random.uniform(now_x - spread_points, now_x + spread_points), 3)
    return rand_x



def algorithm_of_bees(x_min, x_max, x_step, y_min,y_max, y_step, number_of_bees, time,lambda_func):
    # Пчёлы-разведчики
    scout_bees = []
    #_i
    for i in range(number_of_bees):
        rand_x = round(random.uniform(x_min, x_max), 3)
        rand_y = round(random.uniform(y_min, y_max), 3)
        z = round(lambda_func(rand_x, rand_y), 3)
        scout_bees.append([[rand_x, rand_y], z])
    # Результат первой разведки
    sort_scout_bees = sorted(scout_bees, key=lambda x: x[1])

    # Количество лучших зон
    number_best_zone = 3
    # Количество перспективных зон
    number_perspective_zone = 5
    # Разброс точек
    spread_points = 5
    # Список лучших точек в каждом вылете
    history_best_point = []
    # запомним лучшую точку (минимальную)
    best_point = sort_scout_bees[0]
    for i in range(time):
        # Запоменим лучшую точку
        for item in sort_scout_bees[0:5]:
            new_item = [item[0][0], item[0][1], item[1]]
            history_best_point.append(new_item)

        # Запишем лучшие зоны
        best_zones = []
        # Проверяем
        if best_point[1] > sort_scout_bees[0][1]:
            best_point = sort_scout_bees[0]

        # Запишем перспективные зоны
        perspective_zones = []
        # новая группа разведчиков
        new_scout_beens = []
        for i in range(number_best_zone):
            best_zones.append(sort_scout_bees[i][0])

        for i in range(number_perspective_zone):
            perspective_zones.append(sort_scout_bees[number_best_zone + i][0])

        val_best, val_persp = divide_bees_by_group(number_best_zone, number_perspective_zone, number_of_bees)

        for x, y in best_zones:
            for i in range(val_best):
                rand_x = round(create_new_point(x_min, x_max, x, spread_points), 3)
                rand_y = round(create_new_point(y_min, y_max, y, spread_points), 3)

                z = round(lambda_func(rand_x, rand_y), 3)
                new_scout_beens.append([[rand_x, rand_y], z])

        for x, y in perspective_zones:
            for i in range(val_persp):
                rand_x = round(create_new_point(x_min, x_max, x, spread_points), 3)
                rand_y = round(create_new_point(y_min, y_max, y, spread_points), 3)

                z = round(lambda_func(rand_x, rand_y), 3)
                new_scout_beens.append([[rand_x, rand_y], z])
        # Отсортируем новые точки
        sort_scout_bees = sorted(new_scout_beens, key=lambda x: x[1])

    return history_best_point, best_point