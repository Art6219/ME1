import numpy as np
import matplotlib.pyplot as plt

from rigidez_global import rigidez_global
from forca import forca
from cc_lagrange import cc_lagrange
from cc_exc_linha import cc_exc_linha
from cc_1_linha import cc_1_linha
from pos_proc import pos_proc
from plot import plot


def main(coord, conect, Loads, cc, VE, Vv, hip, ele_type, plot_original, plot_desloc, plot_nodes_original, plot_nodes_desloc):

      # Cálculos Iniciais
      nn = len(coord)               # Número de Nós
      ne = len(conect)              # Número de Elementos

      # Processamento (Matriz de Rigidez Global, Vetor de Forças e Vetor de Deslocamentos)
      K = rigidez_global(nn, ne, coord, conect, VE, Vv, hip, ele_type)

      F = forca(nn, Loads)

      Ka, Fa = cc_lagrange(nn, cc, K, F)
      Ua = np.linalg.solve(Ka, Fa)
      Ua1 = Ua[0: 3*nn]

      # Kf, Ff = cc_exc_linha(nn, cc, K, F)
      # Ua2 = np.matmul(np.linalg.inv(Kf), Ff)

      # Kn, Fn = cc_1_linha(nn, cc, K, F)
      # Ua3 = np.matmul(np.linalg.inv(Kn), Fn)

      # Pós-Processamento (Cálculo dos Esforços e Tensões nos Elementos)
      eps, sigmas = pos_proc(coord, conect, ele_type, ne, Ua1, VE, Vv, hip)
      
      # Plot dos resultados
      plot(coord, conect, ne, nn, Ua1, sigmas, plot_original, plot_desloc, plot_nodes_original, plot_nodes_desloc)


      return Ua1, eps, sigmas




