import numpy as np
from scipy import integrate
import random
import copy
from typing import *


class Solver:

    def __init__(self, num_swarm: int, num_iterations: int, fuel: float, locations: list
                 , resturant_location: list):
        self.num_swarm = num_swarm
        self.num_iterations = num_iterations
        self.locations = locations
        self.resturant_location = resturant_location
        self.speed = []
        self.fuel = fuel
        self.fuel_cons_per_100km = 20
        self.petrol_locations = []
        self.gBest = []
        self.gBest_cost = 0

    def swap(self, lst, n, m):
        buff = lst[n-1]
        lst[n-1] = lst[m-1]
        lst[m-1] = buff
        return lst

    def random_petrol_location(self):
        petrol_loc = []
        x_lst = []
        y_lst = []
        x_lst.append(self.resturant_location[0])
        y_lst.append(self.resturant_location[1])

        for loc in self.locations:
            x_lst.append(loc[0])
            y_lst.append(loc[1])

        x_max, y_max = max(x_lst), max(y_lst)
        x_min, y_min = min(x_lst), min(y_lst)

        x_range = list(np.linspace(x_min, x_max, 100))
        y_range = list(np.linspace(y_min, y_max, 100))

        for i in range(3):
            rand_x = random.sample(x_range, k=1)
            rand_y = random.sample(y_range, k=1)
            petrol_loc.append([round(rand_x[0], 14), round(rand_y[0], 14)])

        self.petrol_locations = petrol_loc

    def diff(self, a, b):
        list_of_diff = []
        b_buff = copy.deepcopy(b)
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
                    list_of_diff.append([i+1, ind+1])
                    self.swap(b_buff, i+1, ind+1)
        return list_of_diff

    def generate_speed(self, t):
        time = []
        speed = []
        vel = 60*1000/3600          # m/s
        time = np.linspace(0, t, t*10)
        speed = np.abs(np.sin(0.5*time))*vel

        return speed, time

    def calculate_time(self, route):
        speed, time = self.generate_speed(int(route*100))
        pos = integrate.cumtrapz(speed, time, initial=0)
        t = np.interp(route, pos, time)

        return t

    def route_between_points(self, point1, point2):
        route = np.sqrt(np.power(point1[0] - point2[0], 2) + np.power(point1[1] - point2[1], 2))
        return route

    def calculate_part_cost(self, part, lst_of_points, petrol_locations = []):
        route = 0
        for i in range(len(part)):
            if i == 0:
                if part[i] < 10:
                    route += self.route_between_points(lst_of_points[part[i]-1], self.resturant_location)
                else:
                    route += self.route_between_points(petrol_locations[part[i] - 10], self.resturant_location)

            if i == len(part) - 1:
                if part[i] < 10:
                    route += self.route_between_points(lst_of_points[part[i]-1], self.resturant_location)
                else:
                    route += self.route_between_points(petrol_locations[part[i] - 10], self.resturant_location)
            else:
                if part[i] < 10:
                    if part[i+1] >= 10:
                        route += self.route_between_points(lst_of_points[part[i] - 1], petrol_locations[part[i + 1] - 10])
                    else:
                        route += self.route_between_points(lst_of_points[part[i]-1], lst_of_points[part[i+1]-1])
                else:
                    route += self.route_between_points(petrol_locations[part[i] - 10], lst_of_points[part[i + 1] - 1])
        return route

    def calculate_full_cost(self, lst_of_part, lst_of_points):
        lst_of_cost = []
        for i in range(len(lst_of_part)):
            cal = self.calculate_part_cost(lst_of_part[i], lst_of_points)
            lst_of_cost.append(cal)
        return lst_of_cost

    def calculate_pizza_temp(self,delivery_time):
        if delivery_time <= 10:
            return 80
        elif delivery_time > 40:
            return 20
        else:
            return np.floor(800/delivery_time)

    def calculate_pizza_temp_tab(self,delivery_time_tab):
        pizza_temp_tab = []
        for i in delivery_time_tab:
            pizza_temp_tab.append(self.calculate_pizza_temp(i))
        return pizza_temp_tab

    def add_diff(self, diff, dict):
        check = False
        if diff:
            for p1 in range(len(diff)):  # Dodawanie powyższych predkosci do predkosci wcześniejszej
                dict.append(diff[p1])

    def is_fuel_enough(self, particle):
        if particle:
            particle_cost = self.calculate_part_cost(particle, self.locations)*111
            fuel_need = particle_cost / 100 * self.fuel_cons_per_100km

            route = particle
            if fuel_need + 5 < self.fuel:
                return len(particle)

            del route[-1]
            return self.is_fuel_enough(route)
        else:
            return 0

    def count_time(self):
        delivery_time = []
        route = 0
        time = 0
        for i in range(len(self.gBest)):
            if i == 0:
                if self.gBest[i] < 10:
                    route += 1000 * 111  * self.route_between_points(self.resturant_location, self.locations[self.gBest[i] - 1])
                else:
                    route += 1000 * 111 * self.route_between_points(self.resturant_location, self.petrol_locations[self.gBest[i] - 10])
                time = self.calculate_time(route)
                time = time/60 + (5 * (i+1))
                delivery_time.append(np.around(time,decimals=2))

            else:
                if self.gBest[i] >= 10:
                    route += 1000 * 111 * self.route_between_points(self.locations[self.gBest[i-1] - 1], self.petrol_locations[self.gBest[i] - 10])
                elif self.gBest[i-1] >= 10:
                    route += 1000 * 111 * self.route_between_points(self.petrol_locations[self.gBest[i - 1] - 10], self.locations[self.gBest[i] - 1])
                else:
                    route += 1000 * 111 * self.route_between_points(self.locations[self.gBest[i - 1] - 1], self.locations[self.gBest[i] - 1])

                time = self.calculate_time(route)
                time = time/60 + (5 * (i+1))

                delivery_time.append(np.around(time, decimals=2))
        return delivery_time

    def solve(self):
        list_of_particle = []
        dict_of_vel = {}
        list_of_pBest = []
        cnt = 0

        l = len(self.locations)

        self.gBest = 0

        self.random_petrol_location()

        for i in range(self.num_swarm):  # Losowanie stada i predkosci
            list_of_particle.append(random.sample(range(1, l + 1), k=l))
            dict_of_vel[i] = [(random.sample(range(1, l + 1), k=2)), (random.sample(range(1, l + 1), k=2))]

        list_of_pBest = copy.deepcopy(list_of_particle)  # Obliczanie kosztu dla wylosowanego stada
        lst_of_pBest_cost = self.calculate_full_cost(
            list_of_pBest, self.locations)
        self.gBest_cost = min(lst_of_pBest_cost)
        index_gBest = lst_of_pBest_cost.index(self.gBest_cost)
        self.gBest = list_of_pBest[index_gBest]



        for i in range(self.num_iterations):
            for it in range(self.num_swarm):
                diff1 = self.diff(list_of_particle[it], list_of_pBest[it])  # Wyznaczanie różnic: cząsteczka - pBest [x(i) - pBest]
                diff2 = self.diff(list_of_particle[it], self.gBest)
                # cząsteczka - gBest [x(i) - gBest]
                self.add_diff(diff1, dict_of_vel[it])
                self.add_diff(diff2, dict_of_vel[it])
                for el in range(len(dict_of_vel[it])):
                    if dict_of_vel[it][el]:  # Zastosowanie predkosci dla stada
                        list_of_particle[it] = self.swap(
                            list_of_particle[it], dict_of_vel[it][el][0], dict_of_vel[it][el][1])
            costs = self.calculate_full_cost(list_of_particle, self.locations)
            for it in range(self.num_swarm):  # Aktualizowanie pBest oraz gBest
                if costs[it] < lst_of_pBest_cost[it]:
                    list_of_pBest[it] = copy.deepcopy(list_of_particle[it])
                    lst_of_pBest_cost[it] = costs[it]
                if costs[it] < self.gBest_cost:
                    self.gBest = copy.deepcopy(list_of_particle[it])
                    self.gBest_cost = costs[it]
                    cnt = i+1

        fuel_enough = self.is_fuel_enough(copy.copy(self.gBest))

        if fuel_enough < len(self.gBest):
            best = []
            current_cost = np.inf
            for i in range(fuel_enough + 1):
                for p in range(len(self.petrol_locations)):
                    route = copy.copy(self.gBest)
                    route.insert(i, p + 10)
                    cost = self.calculate_part_cost(route, self.locations, self.petrol_locations)
                    if current_cost == np.inf or cost < current_cost:
                        current_cost = cost
                        best = route


            self.gBest = best
            self.gBest_cost = current_cost * 111

        else:
            self.gBest_cost *=111


        del_time = self.count_time()
        pizza_temp = self.calculate_pizza_temp_tab(del_time)
        fuel_used = fuel_need = self.gBest_cost / 100 * self.fuel_cons_per_100km
        fuel_used = np.around(fuel_used, 2)

        return del_time, pizza_temp, fuel_used
