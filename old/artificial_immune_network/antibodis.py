import numpy


class Antibodies:
  """
    Класс, описывающий один антиген
  """

  def __init__(self, immune_network):
    """

    :param immune_network: - Иммунная сеть содержащая такие параметра как: размер области определения функции и саму функцию
    """

    self.immune_network = immune_network
    self.__currentPosition = self.__getInitPosition()

  def __getInitPosition(self):
    """
    метод генерации координат
    :return: - Возвращает список координат
    """
    return numpy.random.rand(self.immune_network.dimension) * (
        self.immune_network.maxvalues - self.immune_network.minvalues) + self.immune_network.minvalues

  def corretPosition(self):
    """
    Проверяет на выход за границы
    :return:
    """
    self.__currentPosition = numpy.clip(self.__currentPosition, self.immune_network.minvalues,
                                        self.immune_network.maxvalues)

  def mutation(self):
    """
    Мутирует антиген
    :return:
    """
    self.__currentPosition = self.__currentPosition + (
          numpy.random.rand(self.immune_network.dimension) - numpy.array(-0.5[:])) * self.immune_network.alfa_mutation
    self.corretPosition()

  def getValue(self):
    """
    Метод подсчитывающий значение антигена
    :return: - float значение
    """
    return self.immune_network.calcFuncion(self.__currentPosition)
