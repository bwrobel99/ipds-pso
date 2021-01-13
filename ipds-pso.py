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
    #print(s.gBest)
    #print(s.gBest_cost)
    right_order = s.gBest
    graph = Graph()
    longitudes , latitudes = graph.upgrade_points(restaurant_loc=restaurant_loc, right_order=right_order, lst_of_points=lst_of_points)
    graph.show_graph(longitudes=longitudes, latitudes=latitudes)
    '''
    maps_directory = "./maps"
    f = open(os.path.join(maps_directory, 'uno_coor.txt'), "r")
    splitted = f.read().split(' ')
    dct = {}
    for elem in range(0,len(splitted)-1,2):
        dct[splitted[elem]] = float(splitted[elem+1])
    bbox = []
    for value in dct.values():
        bbox.append(value)

    ordered_points = []
    for order in s.gBest:
        if order == s.gBest[0]:
            ordered_points.append(restaurant_loc)
        for index, point in enumerate(lst_of_points):
            if order == (index + 1):
                ordered_points.append(point)
                if order == s.gBest[-1]:
                    ordered_points.append(restaurant_loc)

    longitudes = []
    latitudes = []
    for coor in ordered_points:
        longitudes.append(coor[0])
        latitudes.append(coor[1])


# plotowanie
    map = plt.imread(os.path.join(maps_directory, 'uno.png'))
    fig, ax = plt.subplots(figsize = (8,7))
    #ax.scatter(longitudes,latitudes, zorder = 1, alpha = 0.8, c='r', s=10)
    #ax.scatter(petrol_longitudes, petrol_latitudes, zorder=1, alpha=1, c='y', s=30, marker = 'D')
    #ax.scatter(restaurant_loc[0], restaurant_loc[1], zorder = 1, alpha = 1, c='b', s=30, marker = 's')
    ax.plot(longitudes,latitudes, zorder = 1, alpha = 0.8, ls = '--', c = 'r', marker = 'D')
    for i in range(len(longitudes)-1):
        if i == 0:
            ax.annotate('Pozycja restauracji', xy=(longitudes[i], latitudes[i]))
        else:
            ax.annotate(f'#{i}', xy=(longitudes[i], latitudes[i]))

    ax.set_title('Trasa Pana Kierowcy')
    ax.set_xlim(bbox[0], bbox[1])
    ax.set_ylim(bbox[2], bbox[3])

    ax.imshow(map, zorder = 0, extent=bbox, aspect='equal')
    plt.show()
    '''
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
