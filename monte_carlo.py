#!/usr/bin/python3

import numpy as np

def monte_carlo_simulation(num):
    circle_count = 0

    for i in np.arange(num):
        new_point = np.array([2.*(np.random.random()-0.5),2*(np.random.random()-0.5)])

        if np.linalg.norm(new_point) < 1:
            circle_count += 1

    return circle_count