from math import *
import random as rnd

class Unit:
    def __init__(self,x_min , x_max,currentVelocityRatio, localVelocityRatio, globalVelocityRatio, function):
        # область поиска
        self.start = x_min
        self.end = x_max
        # коэффициенты для изменения скорости
        self.currentVelocityRatio = currentVelocityRatio
        self.localVelocityRatio = localVelocityRatio
        self.globalVelocityRatio = globalVelocityRatio
        # функция
        self.function = function
        # лучшая локальная позиция
        self.localBestPos = self.getFirsPos()
        self.localBestScore = self.function(*self.localBestPos)
        # текущая позиция
        self.currentPos = self.localBestPos[:]
        self.score = self.function(*self.localBestPos)
        # значение глобальной позиции
        self.globalBestPos = []
        # скорость
        self.velocity = self.getFirstVelocity()

    def getFirstVelocity(self):
        """ Метод для задания первоначальной скорости"""
        minval = -(self.end - self.start)
        maxval = self.end - self.start
        return [rnd.uniform(minval, maxval), rnd.uniform(minval, maxval)]

    def getFirsPos(self):
        """ Метод для получения начальной позиции"""
        return [rnd.uniform(self.start, self.end), rnd.uniform(self.start, self.end)]

    def nextIteration(self):
        """ Метод для нахождения новой позиции частицы"""
        # случайные данные для изменения скорости
        rndCurrentBestPosition = [rnd.random(), rnd.random()]
        rndGlobalBestPosition = [rnd.random(), rnd.random()]
        # делаем перерасчет скорости частицы исходя из всех введенных параметров
        velocityRatio = self.localVelocityRatio + self.globalVelocityRatio
        commonVelocityRatio = 2 * self.currentVelocityRatio / abs(
            2 - velocityRatio - sqrt(velocityRatio ** 2 - 4 * velocityRatio))
        multLocal = list(map(lambda x: x * commonVelocityRatio * self.localVelocityRatio, rndCurrentBestPosition))
        betweenLocalAndCurPos = [self.localBestPos[0] - self.currentPos[0], self.localBestPos[1] - self.currentPos[1]]
        betweenGlobalAndCurPos = [self.globalBestPos[0] - self.currentPos[0],
                                  self.globalBestPos[1] - self.currentPos[1]]
        multGlobal = list(map(lambda x: x * commonVelocityRatio * self.globalVelocityRatio, rndGlobalBestPosition))
        newVelocity1 = list(map(lambda coord: coord * commonVelocityRatio, self.velocity))
        newVelocity2 = [coord1 * coord2 for coord1, coord2 in zip(multLocal, betweenLocalAndCurPos)]
        newVelocity3 = [coord1 * coord2 for coord1, coord2 in zip(multGlobal, betweenGlobalAndCurPos)]
        self.velocity = [coord1 + coord2 + coord3 for coord1, coord2, coord3 in
                         zip(newVelocity1, newVelocity2, newVelocity3)]
        # передвигаем частицу и смотрим, какое значение целевой фунции получается
        self.currentPos = [coord1 + coord2 for coord1, coord2 in zip(self.currentPos, self.velocity)]
        newScore = self.function(*self.currentPos)
        if newScore < self.localBestScore:
            self.localBestPos = self.currentPos[:]
            self.localBestScore = newScore
        return newScore


class Swarm:

    def __init__(self,x_min , x_max, x_step , y_min ,y_max , y_step, sizeSwarm,
                 currentVelocityRatio,
                 localVelocityRatio,
                 globalVelocityRatio,
                 numbersOfLife,
                 function,
                 start,
                 end):
        # размер популяции частиц
        self.sizeSwarm = sizeSwarm
        # коэффициенты изменения скорости
        self.currentVelocityRatio = currentVelocityRatio
        self.localVelocityRatio = localVelocityRatio
        self.globalVelocityRatio = globalVelocityRatio
        # количество итераций алгоритма
        self.numbersOfLife = numbersOfLife
        # функция для поиска экстремума
        self.function = function
        # область поиска
        self.start = start
        self.end = end
        # рой частиц
        self.swarm = []
        # данные о лучшей позиции
        self.globalBestPos = []
        self.globalBestScore = float('inf')
        # создаем рой
        self.createSwarm()

    def createSwarm(self):
        """ Метод для создания нового роя"""
        pack = [self.start, self.end, self.currentVelocityRatio, self.localVelocityRatio, self.globalVelocityRatio,
                self.function]
        self.swarm = [Unit(*pack) for _ in range(self.sizeSwarm)]
        # пересчитываем лучшее значение для только что созданного роя
        for unit in self.swarm:
            if unit.localBestScore < self.globalBestScore:
                self.globalBestScore = unit.localBestScore
                self.globalBestPos = unit.localBestPos

    def f(self, x, y):
        min_val = self.function(x[0], y[0])
        min_point = [x[0], y[0]]
        for i in range(len(x)):
            if min_val > self.function(x[i], y[i]):
                min_val = self.function(x[i], y[i])
                # Тут изменены точки для функций отрисовки точек #
                min_point = [x[i], y[i], min_val]
        return min_point

    def startSwarm(self):
        """ Метод для запуска алгоритма"""
        list_of_population = []

        dataForGIF = []
        for _ in range(self.numbersOfLife):
            oneDataX = []
            oneDataY = []

            population = [] # Создание популяции для одной итерации
            for unit in self.swarm:
                # Создание двухмерной частицы и помещение ее в ее же популяцию
                population.append([unit.currentPos[0],unit.currentPos[1]])

                oneDataX.append(unit.currentPos[0])
                oneDataY.append(unit.currentPos[1])
                unit.globalBestPos = self.globalBestPos
                score = unit.nextIteration()
                if score < self.globalBestScore:
                    self.globalBestScore = score
                    self.globalBestPos = unit.localBestPos
            dataForGIF.append([oneDataX, oneDataY])
            list_of_population.append(population)

        points = []
        for x, y in dataForGIF:
            points.append(self.f(x, y))
        return list_of_population

# my_function = choise_function("Функция Экли")
# swarm = Swarm(x_min = 2 , x_max = 4, x_step = 0.2 , y_min = -2 ,y_max =2  , y_step = 0.2,sizeSwarm=10,
#               currentVelocityRatio=0.5,
#               localVelocityRatio=2,
#               globalVelocityRatio=5,
#               numbersOfLife=100,
#               function=my_function,
#               start=-10,
#               end=10)

# # Запускаем алгоритм оптимизации
# result = swarm.startSwarm()
# print(result)