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
    s = Solver(25, 25, 5.5, lst_of_points, restaurant_loc, petrol_loactions)
    delivery_time, pizza_temperature, used_fuel = s.solve()
    print(f"Kolejność dostawy pizzy: {s.gBest}")
    print(f"Czas dostawy [min]: {delivery_time}")
    print(f"Temperatura pizzy [st.C]: {pizza_temperature}")
    print(f"Długość trasy [km]: {np.around(s.gBest_cost,2)}")
    print(f"Zużyte paliwo: {used_fuel}")
    right_order = s.gBest
    graph = Graph()
    longitudes , latitudes = graph.upgrade_points(restaurant_loc=restaurant_loc, right_order=right_order, lst_of_points=lst_of_points, petrol_loactions=petrol_loactions)
    graph.show_graph(longitudes=longitudes, latitudes=latitudes, petrol_locations=petrol_loactions, restaurant_loc=restaurant_loc, lst_of_points=lst_of_points)

if __name__ == "__main__":
    main()
