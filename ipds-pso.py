from elements.particle import Particle
from elements.solver import Solver
from elements.graph import Graph
from random import random


def main():
    lst_of_points = [[49.981862518527194, 19.948879677062486],
                     [49.9818383674969, 19.948069653078814], [49.98329150894827, 19.946237372007527],
                     [49.98333981650393, 19.946972318011984]]
    restaurant_loc = [49.983351, 19.944778]
    s = Solver(100, 100, lst_of_points, restaurant_loc)
    s.solve()
    print(s.gBest)
    print(s.gBest_cost)


if __name__ == "__main__":
    main()
