import numpy as np


def load_distribuida(L, q1, q2, x):

    f = (q2 - q1)/L*x + q1

    return f


def careg_dist(n, L, q1, q2):

    passo = np.linspace(0, L, n + 1)

    load_dist = []
    for i in range(len(passo) - 1):

        f1 = load_distribuida(L, q1, q2, passo[i])
        f2 = load_distribuida(L, q1, q2, passo[i + 1])

        load_dist.append([i, f1, f2])

    return load_dist



q1 = -500
q2 = -800
L = 2

n = 1

load_dist = careg_dist(n, L, q1, q2)

print(load_dist)
