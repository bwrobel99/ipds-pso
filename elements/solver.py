import random
import numpy as np


class Solver:
    def __init__(self):
        # self.target = target
        # self.target_error = target_error
        # self.n_particles = n_particles
        self.particles = []
        self.gbest_value = float('inf')
        self.gbest_position = np.array(
            [random.random()*50, random.random()*50])
