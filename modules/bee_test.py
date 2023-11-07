import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from functions import choise_function
import random

def fitness(points,fitness_function):
	fitness_values = [fitness_function(*point) for point in points]
	print("Шаг 3")
	print (fitness_values)
	return fitness_values

def generate_random_points(So_quantity,fitness_function,x_min,x_max,y_min,y_max,x_step,y_step):
	point_list = []
	for i in range(1,So_quantity):
		x = random.uniform(x_min, x_max)
		y = random.uniform(y_min,y_max)

		x = round(x / x_step) * x_step
		y = round(y / y_step) * y_step

		point_list.append(fitness_function(x,y))
	point_list.sort(reverse=True)
	print("Первый шаг")
	print(point_list)

	return (point_list)

def workers_distribution(point_list,Sw_quantity):
	# Разделение точек на Ab и Ap
	Ab_points = point_list[:Ab_quantity]
	Ap_points = point_list[Ab_quantity:Ab_quantity + Ap_quantity]
	if not Ap_points:
		workers_per_Ab = Sw_quantity
		workers_per_Ap = 0
	else:
		workers_per_Ab = Sw_quantity // 2
		workers_per_Ap = Sw_quantity - workers_per_Ab

	# Выбор центров участков
	Ajb_centers = Ab_points[:workers_per_Ab]
	Akp_centers = Ap_points[:workers_per_Ap]
	print("Второй шаг")
	print(Ajb_centers)
	print(Akp_centers)
	return Ajb_centers,Akp_centers


# def fitness(population, fitness_function):
#     x = population[:, 0]
#     y = population[:, 1]
#     return  1/(fitness_function(x, y) + 1e-6)


def bee_swarm(So_quantity, Sw_quantity,Ab_quantity,Ap_quantity, fitness_function, x_min, x_max, y_min, y_max, x_step, y_step):
	points = generate_random_points(So_quantity,fitness_function,x_min,x_max,y_min,y_max,x_step,y_step)
	workers_distribution(points,Sw_quantity)
	fitness(points,fitness_function)
	pass


So_quantity = 20
Sw_quantity = 20
Ab_quantity = 10
Ap_quantity = 10
fitness_function = choise_function("Функция Розенброкка")
x_min = -2
x_max = 2
y_min = -2
y_max = 2
x_step = 0.01
y_step = 0.01

bee_swarm(So_quantity, Sw_quantity,Ab_quantity,Ap_quantity, fitness_function, x_min, x_max, y_min, y_max, x_step, y_step)
#So - скауты
#Sw - рабочие
#Множество элитных участков Аb, мн-во перспективных участков Ар 

# 1 – генерируем случайные точки в пространстве поиска xi причем i=[1,So], 
# отправляем эти точки пчел разведчиков Sio, вычисляем значения целовой фio, 
# сортируем величины по убыванию и представляем в виде линейного списка,


