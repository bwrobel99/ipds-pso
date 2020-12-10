import numpy as np
import random
import copy
from typing import *


class Solver:

    def __init__(self, num_swarm: int, num_iterations: int, locations: List, resturant_location: List):
        self.num_swarm = num_swarm
        self.num_iterations = num_iterations
        self.locations = locations
        self.resturant_location = resturant_location
        self.gBest = []
        self.gBest_cost = 0

    def swap(self, lst, n, m):
        buff = lst[n-1]
        lst[n-1] = lst[m-1]
        lst[m-1] = buff
        return lst

    def diff(self, a, b):
        list_of_diff = []
        b_buff = b[:]
        if len(a) != len(b):
            print("Blad! Różne długości tablic")
            return -1
        for i in range(len(a)-1):
            if a == b_buff:
                break
            else:
                if a[i] != b_buff[i]:
                    ind = b_buff.index(a[i])
                    if ind == -1:
                        return -1
                    list_of_diff.append([i+1, ind])
                    self.swap(b_buff, i+1, ind)
        return list_of_diff

    def calculate_part_cost(self, part, lst_of_points):
        route = 0
        for i in range(len(part)):
            if i == 0:
                route += np.sqrt(np.power(lst_of_points[part[i]-1][0] - self.resturant_location[0], 2) +
                                 np.power(lst_of_points[part[i]-1][1] - self.resturant_location[1], 2))
            if i == len(part) - 1:
                route += np.sqrt(np.power(lst_of_points[part[i]-1][0] - self.resturant_location[0], 2) +
                                 np.power(lst_of_points[part[i]-1][1] - self.resturant_location[1], 2))
            else:
                route += np.sqrt(np.power(lst_of_points[part[i]-1][0] - lst_of_points[part[i+1]-1][0], 2) +
                                 np.power(lst_of_points[part[i]-1][1] - lst_of_points[part[i+1]-1][1], 2))
        return route

    # pkt poczatkowy to [0,0]

    def calculate_full_cost(self, lst_of_part, lst_of_points):
        lst_of_cost = []
        for i in range(len(lst_of_part)):
            cal = self.calculate_part_cost(lst_of_part[i], lst_of_points)
            lst_of_cost.append(cal)
        return lst_of_cost

    def solve(self):
        list_of_particle = []
        dict_of_vel = {}
        list_of_pBest = []

        l = len(self.locations)

        self.gBest = 0

        for i in range(self.num_swarm):                                     #   Losowanie stada i predkosci
            list_of_particle.append(random.sample(range(1, l+1), k=l))
            dict_of_vel[i] = [(random.sample(range(1, l+1), k=2))]

        list_of_pBest = copy.deepcopy(list_of_particle)                     #   Obliczanie kosztu dla wylosowanego stada
        lst_of_pBest_cost = self.calculate_full_cost(
            list_of_pBest, self.locations)
        self.gBest_cost = min(lst_of_pBest_cost)
        index_gBest = lst_of_pBest_cost.index(self.gBest_cost)
        self.gBest = list_of_pBest[index_gBest]

        check = False                                                       #   Flaga - czy skladowa predkosci sie juz powtarza
        for i in range(self.num_iterations):
            for it in range(self.num_swarm):
                diff1 = self.diff(list_of_particle[it], list_of_pBest[it])  #   Wyznaczanie różnic: cząsteczka - pBest [x(i) - pBest]
                diff2 = self.diff(list_of_particle[it], self.gBest)         #                       cząsteczka - gBest [x(i) - gBest]
                if diff1:
                    for p1 in range(len(diff1)):                            #   Dodawanie powyższych predkosci do predkosci wcześniejszej
                        for c1 in range(len(dict_of_vel[it])):              #   Wedlug wzoru: v(i+1) = v(i) + [x(i) - pBest] + [x(i) - g Best]
                            check = False
                            if dict_of_vel[it][c1]:
                                if dict_of_vel[it][c1][0] == diff1[p1][0] and dict_of_vel[it][c1][1] == diff1[p1][1]:
                                    dict_of_vel[it][c1].clear()             #   Sprawdzanie powtorzenia dla diff 1
                                    check = True
                                elif dict_of_vel[it][c1][0] == diff1[p1][1] and dict_of_vel[it][c1][1] == diff1[p1][0]:
                                    dict_of_vel[it][c1].clear()
                                    check = True
                        if not check:
                            dict_of_vel[it].append(diff1[p1])
                if diff2:
                    for p2 in range(len(diff2)):
                        check = False
                        for c2 in range(len(dict_of_vel[it])):
                            if dict_of_vel[it][c2]:
                                if dict_of_vel[it][c2][0] == diff2[p2][0] and dict_of_vel[it][c2][1] == diff2[p2][1]:
                                    del dict_of_vel[it][c2]
                                    check = True
                                    break
                                elif dict_of_vel[it][c2][0] == diff2[p2][1] and dict_of_vel[it][c2][1] == diff2[p2][0]:
                                    del dict_of_vel[it][c2]
                                    check = True
                                    break
                        if not check:
                            dict_of_vel[it].append(diff2[p2])
                for el in range(len(dict_of_vel[it])):
                    if dict_of_vel[it][el]:                         #   Zastosowanie predkosci dla stada
                        list_of_particle[it] = self.swap(
                                            list_of_particle[it], dict_of_vel[it][el][0], dict_of_vel[it][el][1])
            costs = self.calculate_full_cost(list_of_particle, self.locations)
            for it in range(self.num_swarm):                        #   Aktualizowanie pBest oraz gBest
                if costs[it] < lst_of_pBest_cost[it]:
                    list_of_pBest[it] = list_of_particle[it]
                    lst_of_pBest_cost[it] = costs[it]
                if costs[it] < self.gBest_cost:
                    self.gBest = list_of_particle[it]
