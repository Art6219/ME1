import numpy as np
import matplotlib.pyplot as plt

from pre_proc import pre_proc
from matriz_rigidez import matriz_rigidez
from forca import forca
from cc_lagrange import cc_lagrange
from cc_exc_linha import cc_exc_linha
from cc_1_linha import cc_1_linha
from esforcos import esforcos
from plot import plot


def main(coord, conect, Loads, Load_dist, cc, VE, VA, VI):

      # Cálculos Inciais
      nn = len(coord)               # Número de Nós
      ne = len(conect)              # Número de Elementos

      # Pré-Processamento (Cálculo do comprimento e rotação dos elementos)
      VL, Vr = pre_proc(coord, conect, ne)

      # Processamento (Matriz de Rigidez Global, Vetor de Forças e Vetor de Deslocamentos)
      K = matriz_rigidez(nn, ne, conect, VE, VA, VI, VL, Vr)

      F = forca(conect, nn, Loads, Load_dist, VL, Vr)

      Ka, Fa = cc_lagrange(nn, cc, K, F)
      Ua = np.linalg.solve(Ka, Fa)
      Ua1 = Ua[0: 3*nn]

      Kf, Ff = cc_exc_linha(nn, cc, K, F)
      Ua2 = np.matmul(np.linalg.inv(Kf), Ff)

      Kn, Fn = cc_1_linha(nn, cc, K, F)
      Ua3 = np.matmul(np.linalg.inv(Kn), Fn)

      # Pós-Processamento (Cálculo dos Esforços e Tensões nos Elementos)
      N, V, M = esforcos(nn, ne, conect, VE, VA, VL, VI, Vr, Ua1, Load_dist)

      r = 0.01          # PROVISÓRIO Distância ao centroide
      Sigma = []
      for i in range(len(VA)):

            s_xx_N = N[i]/VA[i]
            s_xy_V = max(max(V[i]), abs(min(V[i])))/VA[i]
            s_xx_M = max(max(M[i]), abs(min(M[i])))*r/VI[i]

            Sigma.append([s_xx_N, s_xy_V, s_xx_M])

      # Plot dos resultados
      plot(coord, conect, ne, nn, Ua1)


      return Ua1, Ua2, Ua3, Sigma



