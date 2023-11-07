import numpy
import numpy.random

from modules.particles_swarm.swarm import Swarm


class Swarm_Function(Swarm):
  def __init__(self,
               swarmsize,
               minvalues,
               maxvalues,
               currentVelocityRatio,
               localVelocityRatio,
               globalVelocityRatio,
               ourFunction):
    self.__ourFunction = ourFunction
    Swarm.__init__(self,
                   swarmsize,
                   minvalues,
                   maxvalues,
                   currentVelocityRatio,
                   localVelocityRatio,
                   globalVelocityRatio)

  def getOurFunction(self):
    return self.__ourFunction

  def _finalFunc(self, position):
    function = self.getOurFunction()(position[0], position[1])
    penalty = self._getPenalty(position, 10000.0)

    return function + penalty


if __name__ == "__main__":
  iterCount = 1000

  dimension = 2
  swarmsize = 200

  minvalues = numpy.array([-5.12] * dimension)
  maxvalues = numpy.array([5.12] * dimension)

  currentVelocityRatio = 0.5
  localVelocityRatio = 2.0
  globalVelocityRatio = 5.0

  ourFunction = lambda x, y: (1 - x) ** 2 + 100 * (y - x ** 2) ** 2

  swarm = Swarm_Function(swarmsize,
                         minvalues,
                         maxvalues,
                         currentVelocityRatio,
                         localVelocityRatio,
                         globalVelocityRatio,
                         ourFunction
                         )

  for n in range(iterCount):
    # как выводить множество точек
    swarm.nextIteration()
