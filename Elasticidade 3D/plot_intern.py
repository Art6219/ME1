import numpy as np
import matplotlib.pyplot as plt


def plot_intern(F, Lx, Ly, Lz, x, nz, tensao_xx, tensao_xy, plot_momento, plot_cortante):

    # Cálculos prévios
    h = Lz/nz
    s = []
    for i in range(nz):
        s.append(h/2 + h*i - Lz/2)

    s.reverse()

    z = np.linspace(-Lz/2, Lz/2, 20)

    # Tensão de Flexão
    s_xx = 12*(F*Lx - F*x)*z/(Ly*Lz**3)

    # Tensão Cortante
    s_xy = 12*F/(Ly*Lz**3) * 0.5*(Lz**2/4 - z**2)

    if plot_momento is True:

        plt.figure()
        plt.scatter(tensao_xx, s, color = "red", label = "Valores Numéricos")
        plt.plot(s_xx, z, label = "Valores Analíticos")
        plt.legend()
        plt.grid()

    if plot_cortante is True:

        plt.figure()
        plt.scatter(tensao_xy, s, color = "red", label = 'Valores Numéricos')
        plt.plot(s_xy, z, label = "Valores Analíticos")
        plt.legend()
        plt.grid()

    sigma_xx = 12*(F*Lx - F*x)*s[0]/(Ly*Lz**3)
    sigma_xy = 12*F/(Ly*Lz**3) * 0.5*(Lz**2/4 - 0**2)


    return sigma_xx, sigma_xy

