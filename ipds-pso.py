from elements.solver import Solver
from elements.graph import Graph
from random import random
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
import os


def main():

    lst_of_points = [[19.9320, 50.0580], [19.945, 50.0685],
                     [19.9431, 50.0590], [19.9270, 50.0632],
                     [19.9370, 50.0600], [19.940, 50.068]]
    restaurant_loc = [19.9383, 50.0634]
    petrol_loactions = [[19.9380, 50.0578], [19.9500, 50.0643], [19.9499, 50.0599]]
    s = Solver(50, 50, lst_of_points, restaurant_loc, petrol_loactions)
    s.solve()
    print(s.gBest)
    print(s.gBest_cost)
    right_order = s.gBest
    graph = Graph()
    longitudes , latitudes = graph.upgrade_points(restaurant_loc=restaurant_loc, right_order=right_order, lst_of_points=lst_of_points, petrol_loactions=petrol_loactions)
    graph.show_graph(longitudes=longitudes, latitudes=latitudes, petrol_locations=petrol_loactions, restaurant_loc=restaurant_loc, lst_of_points=lst_of_points)

    # errors = []
    # bad = []
    # cnt = 0
    # buff = []
    # buff_tab = []
    # for i in range(1,2):
    #     si = Solver(i, 10, lst_of_points, restaurant_loc, petrol_loactions)
    #     for it in range(10):
    #         buff = si.solve()
    #     errors.append(cnt)
    #     bad = []
    #     cnt = 0
    #     print(buff)
    #     print(i)
    # plt.bar(range(1,2),[100 - el for el in errors])
    # plt.title("Skuteczność algorytmu w zależności od liczby iteracji")
    # plt.xlabel("Liczba iteracji")
    # plt.ylabel("Sktueczność algorytmu [%]")
    # plt.show()




if __name__ == "__main__":
    main()
