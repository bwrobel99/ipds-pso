from elements.particle import Particle
from elements.solver import Solver
from elements.graph import Graph
from random import random
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate


def main():
    lst_of_points = [[10, 0],
                     [15, 0], [20, 0],
                     [50, 0]]
    restaurant_loc = [0, 0]
    petrol_loactions = [[1, 0], [2, 0]]
    s = Solver(100, 100, lst_of_points, restaurant_loc, petrol_loactions)
    s.solve()
    print(s.gBest)
    print(s.gBest_cost)

    # time = []
    # speed = []
    # vel = 60/3600
    # time = np.linspace(0, 2400, 24000)
    # speed = np.abs(np.sin(0.05*time)) * vel
    # print(speed)
    # plt.plot(time, speed)
    # plt.show()
    #
    # route = 5  # km
    # del_pos = integrate.cumtrapz(speed, time, initial=0)
    # t = np.interp(2, del_pos, time)
    # print(t)
    # plt.plot(time, del_pos)
    # plt.show()


if __name__ == "__main__":
    main()