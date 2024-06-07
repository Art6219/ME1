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


def main(coord, conect, Loads, cc, VE, VA):

      # Cálculos Iniciais
      nn = len(coord)               # Número de Nós
      ne = len(conect)              # Número de Elementos

      # Pré-Processamento (Cálculo do comprimento e rotação dos elementos)
      VL, Vr = pre_proc(coord, conect, ne)

      # Processamento (Matriz de Rigidez Global, Vetor de Forças e Vetor de Deslocamentos)
      K = matriz_rigidez(nn, ne, conect, VE, VA, VL, Vr)

      F = forca(nn, Loads)

      Ka, Fa = cc_lagrange(nn, cc, K, F)
      Ua = np.linalg.solve(Ka, Fa)
      Ua1 = Ua[0: 2*nn]

      Kf, Ff = cc_exc_linha(nn, cc, K, F)
      Ua2 = np.matmul(np.linalg.inv(Kf), Ff)

      Kn, Fn = cc_1_linha(nn, cc, K, F)
      Ua3 = np.matmul(np.linalg.inv(Kn), Fn)

      # Pós-Processamento (Cálculo dos Esforços e Tensões nos Elementos)
      N = esforcos(ne, conect, VE, VA, VL, Vr, Ua1)

      Sigma = []
      for i in range(len(VA)):
            Sigma.append(N[i]/VA[i])

      # Plot dos resultados
      plot(coord, conect, ne, nn, Ua1)


      return Ua1, N




