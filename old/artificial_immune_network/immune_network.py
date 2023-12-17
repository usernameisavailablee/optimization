from modules.artificial_immune_network.antibodis import Antibodies
import numpy

class ArtificialImmuneNetwork:
  def __init__(self, min_values, max_values, dimension, antibodies_size,count_of_clones,count_of_the_bests,alfa_mutation):
    """
    Класс реализующий работу исскуственной иммунной сети
    :param min_values: - задает минимальную границу размещения антитела
    :param max_values:  - задает максимальную границу размещения антитела
    :param dimension:
    :param antibodies_size:
    """
    self.antibodies_size = antibodies_size

    assert len(min_values) == len(max_values)
    self.alfa_mutation = numpy.array(alfa_mutation[:])
    self.min_values = numpy.array(min_values[:])
    self.max_values = numpy.array(max_values[:])
    self.dimension = dimension
    self.count_of_clones = count_of_clones
    self.count_of_the_bests = count_of_the_bests
    self.antibodies = self.__createNerwork()


  def __createNerwork(self):
    """
    Создать рой из частиц со случайными координатами
    """
    return [Antibodies(self) for _ in range(self.antibodies_size)]




  def nextInteration(self):
    sorted_antibodies = sorted(self.antibodies, key=lambda antibody: antibody.get_value())
    selected_antibodies = sorted_antibodies[:self.count_of_the_bests]
    clones = [selected_antibodies for _ in range(self.count_of_clones)]

    for antibody in clones:
      antibody.mutation()

    sorted_mutation_antibodies = sorted(self.clones, key=lambda antibody: antibody.get_value())
    selected_mutation_antibodies = sorted_mutation_antibodies[:self.count_of_the_bests]

    extended_list_of_antibodies = self.antibodies + selected_mutation_antibodies
    sorted_extended_list_of_antibodies = sorted(self.extended_list_of_antibodies, key=lambda antibody: antibody.get_value())
    self.antibodies = sorted_extended_list_of_antibodies[:self.antibodies_size]


