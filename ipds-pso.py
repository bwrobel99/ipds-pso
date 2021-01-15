from elements.solver import Solver
from elements.graph import Graph
from random import random
import numpy as np
from matplotlib import pyplot as plt
from scipy import integrate
import os


def main():

    lst_of_points = [[19.9320, 50.0580], [19.945, 50.0685],
                     [19.9431, 50.0590], [19.927, 50.0632],
                     [19.9370, 50.0600], [19.940, 50.0682]]
    restaurant_loc = [19.9383, 50.0634]
    petrol_loactions = [[19.9380, 50.0578], [19.9500, 50.0643], [19.9499, 50.0599]]
    s = Solver(25, 25, lst_of_points, restaurant_loc, petrol_loactions)

    s.solve()
    print(s.gBest)
    print(s.gBest_cost)
    right_order = s.gBest
    graph = Graph()
    longitudes , latitudes = graph.upgrade_points(restaurant_loc=restaurant_loc, right_order=right_order, lst_of_points=lst_of_points, petrol_loactions=petrol_loactions)
    graph.show_graph(longitudes=longitudes, latitudes=latitudes, petrol_locations=petrol_loactions, restaurant_loc=restaurant_loc, lst_of_points=lst_of_points)

    # errors = []
    # errors1 = []
    # bad = []
    # cnt = 0
    # cnt1 = 0
    # buff = []
    # buff_tab = []
    # for i in range(20,101,2):
    #     si = Solver(i, 100, lst_of_points, restaurant_loc, petrol_loactions)
    #     for it in range(10):
    #         si.solve()
    #         if si.gBest_cost > 77:
    #             cnt += 10
    #         if si.gBest_cost > 76:
    #             cnt1 += 10
    #     errors.append(cnt)
    #     errors1.append(cnt1)
    #     cnt = 0
    #     cnt1 = 0
    #     print(i)
    # print(errors)
    # print(errors1)
    # plt.bar(range(20,101,2),[100 - el for el in errors])
    # plt.title("Skuteczność algorytmu w zależności od liczby iteracji")
    # plt.xlabel("Liczba iteracji")
    # plt.ylabel("Sktueczność algorytmu [%]")
    # plt.show()
    # plt.figure()
    # plt.bar(range(20, 101, 2), [100 - el for el in errors1])
    # plt.title("Skuteczność algorytmu w zależności od liczby iteracji")
    # plt.xlabel("Liczba iteracji")
    # plt.ylabel("Sktueczność algorytmu [%]")
    # plt.show()





if __name__ == "__main__":
    main()
