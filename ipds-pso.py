from elements.particle import Particle
from elements.solver import Solver
from elements.graph import Graph
from random import random
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
import os


def main():

    lst_of_points = [[19.9320, 50.0580],
                     [19.9431, 50.0590], [19.9270, 50.0632],
                     [19.9370, 50.0600]]
    restaurant_loc = [19.9383, 50.0634]
    petrol_loactions = [[19.9380, 50.0578], [19.9500, 50.0643], [19.9499, 50.0599]]
    s = Solver(100, 100, lst_of_points, restaurant_loc, petrol_loactions)
    s.solve()
    print(s.gBest)
    print(s.gBest_cost * 111)
    right_order = s.gBest
    graph = Graph()
    longitudes , latitudes = graph.upgrade_points(restaurant_loc=restaurant_loc, right_order=right_order, lst_of_points=lst_of_points, petrol_loactions=petrol_loactions)
    graph.show_graph(longitudes=longitudes, latitudes=latitudes, petrol_locations=petrol_loactions, restaurant_loc=restaurant_loc, lst_of_points=lst_of_points)

if __name__ == "__main__":
    main()
