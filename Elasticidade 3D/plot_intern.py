import numpy as np
import matplotlib.pyplot as plt


def plot_intern(F, Lx, Ly, Lz, nz, x):

    # Cálculos prévios
    # x = Lx/2

    z = np.linspace(-Lz/2, Lz/2, 10)

    # Tensão de Flexão
    # s_xx = []
    # s_xx.append(12*(F*Lx - F*x)*z/(Ly*Lz**3))
    s_xx = 12*(F*Lx - F*x)*z/(Ly*Lz**3)

    # Tensão Cortante
    # s_xy = []
    # s_xy.append(12*F/(Ly*Lz**3) * 0.5*(Lz**2/4 - z**2))
    s_xy = 12*F/(Ly*Lz**3) * 0.5*(Lz**2/4 - z**2)

    plt.figure()
    plt.plot(s_xx, z)
    plt.grid()

    plt.figure()
    plt.plot(s_xy, z)
    plt.grid()

