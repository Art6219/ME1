import numpy as np
import matplotlib.pyplot as plt


def gradient(sigmas):

    sigmaxx = []
    for i in sigmas:
        sigmaxx.append(i[0])

    # Normaliza a lista de números para o intervalo [0, 1]
    numeros_normalizados = (np.array(sigmaxx) - min(sigmaxx)) / (max(sigmaxx) - min(sigmaxx))

    # Escolhe um mapa de cores (colormap)
    colormap = plt.get_cmap('coolwarm')  # 'coolwarm' é um exemplo; pode usar outros como 'viridis', 'plasma', etc.

    cores = []
    for n in numeros_normalizados:
        cores.append(colormap(n))

    return cores, sigmaxx
