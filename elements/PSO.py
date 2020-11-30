import numpy as np
import random
import copy


class Particle:
    def __init__(self, position, velocity, pBest):
        self.position = position   # lista -> np. [1,2,3,4,5]; [4,2,5,1,3]
        self.velocity = velocity   # lista par -> np. [[1,2],[2,3],[4,5]]
        self.pBest = pBest         # lista -> [1,2,3,4,5]


def create_swarm(self, n, m):
    for it in range(n):
        rand_pos = []
        rand_vel = []
        for len in range(m):
            rand_pos.append(random.randint(1, m))
            rand_vel.append([random.randint(1, m)])


def swap(lst, n, m):
    buff = lst[n-1]
    lst[n-1] = lst[m-1]
    lst[m-1] = buff
    return lst


def find(lst, key):
    for i in range(len(lst)):
        if lst[i] == key:
            return i+1

    return -1


def diff(a, b):
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
                ind = find(b_buff, a[i])
                if ind == -1:
                    print("Błąd w find()")
                    return -1
                list_of_diff.append([i+1, ind])
                swap(b_buff, i+1, ind)

    return list_of_diff


def calculate_help(part, lst_of_points):
    route = 0
    for i in range(len(part)):
        if i == 0:
            route += np.sqrt(np.power(lst_of_points[part[i]-1][0], 2) +
                             np.power(lst_of_points[part[i]-1][1], 2))
        if i == len(part) - 1:
            route += np.sqrt(np.power(lst_of_points[part[i]-1][0], 2) +
                             np.power(lst_of_points[part[i]-1][1], 2))
        else:
            route += np.sqrt(np.power(lst_of_points[part[i]-1][0] - lst_of_points[part[i+1]-1][0], 2) +
                             np.power(lst_of_points[part[i]-1][1] - lst_of_points[part[i+1]-1][1], 2))
    return route


def calculate(lst_of_part, lst_of_points):          # pkt poczatkowy to [0,0]
    lst_of_cost = []
    for i in range(len(lst_of_part)):
        cal = calculate_help(lst_of_part[i], lst_of_points)
        lst_of_cost.append(cal)
    return lst_of_cost


lst_of_points = [[1, 3], [4, 2], [2, 7], [2, 5]]


def PSO(n, m, l):             # n -> liczebność stada  m -> liczba iteracji   l -> liczba klientow
    list_of_particle = []
    dict_of_vel = {}
    list_of_pBest = []
    gBest = 0

    for i in range(n):
        list_of_particle.append(random.sample(range(1, l+1), k=l))
        dict_of_vel[i] = [(random.sample(range(1, l+1), k=2))]

    list_of_pBest = copy.deepcopy(list_of_particle)
    lst_of_pBest_cost = calculate(list_of_pBest, lst_of_points)
    gBest_cost = min(lst_of_pBest_cost)
    index_gBest = lst_of_pBest_cost.index(gBest_cost)
    gBest = list_of_pBest[index_gBest]
    print(gBest)

    check = False
    for i in range(m):
        for it in range(n):
            diff1 = diff(list_of_particle[it], list_of_pBest[it])
            diff2 = diff(list_of_particle[it], gBest)
            if diff1:
                for p1 in range(len(diff1)):
                    for c1 in range(len(dict_of_vel[it])):
                        check = False
                        if dict_of_vel[it][c1]:
                            if dict_of_vel[it][c1][0] == diff1[p1][0] and dict_of_vel[it][c1][1] == diff1[p1][1]:
                                dict_of_vel[it][c1].clear()
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
                if dict_of_vel[it][el]:
                    list_of_particle[it] = swap(list_of_particle[it], dict_of_vel[it][el][0], dict_of_vel[it][el][1])
        costs = calculate(list_of_particle, lst_of_points)
        for it in range(n):
            if costs[it] < lst_of_pBest_cost[it]:
                list_of_pBest[it] = list_of_particle[it]
                lst_of_pBest_cost[it] = costs[it]
            if costs[it] < gBest_cost:
                gBest = list_of_particle[it]
    return gBest, gBest_cost





PSO(10, 1000, 4)
