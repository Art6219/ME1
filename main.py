import numpy as np

from pre_proc import pre_proc
from matriz_rigidez import matriz_rigidez
from forca import forca
from cc_lagrange import cc_lagrange
from cc_linha import cc_linha
from esforcos import esforcos
from plot import plot


def main():

      # Inputs 1
      coord = [[0, 0],              # Coordenadas dos Pontos
               [0.6, 0],
               [0.6, 0.8],
               [0, 0.8]]

      conect = [[0, 1],             # Conectividades
                [1, 2],
                [2, 3],
                [3, 0],
                [1, 3]]

      nn = len(coord)               # Número de Nós
      ne = len(conect)              # Número de Elementos

      E = 100e3                     # Módulo de Elasticidade
      A = 1                      # Área da Seção

      VE = E * np.ones(ne)
      VA = A * np.ones(ne)

      cc = [[1, 1, 0],              # Condições de Contorno [Nó, GL, Valor]
            [2, 1, 0],
            [2, 2, 0]]

      Loads = [[0, 2, -1000]]       # Forças [Nó, GL, Valor]

      # # Inputs 2
      # coord = [[0, 0],              # Coordenadas dos Pontos
      #          [1, 0],
      #          [0.5, np.sin(np.pi/3)]]

      # conect = [[0, 2],             # Conectividades
      #           [1, 2]]

      # nn = len(coord)               # Número de Nós
      # ne = len(conect)              # Número de Elementos

      # E = 60e3                     # Módulo de Elasticidade
      # A = 1                      # Área da Seção

      # VE = E * np.ones(ne)
      # VA = A * np.ones(ne)

      # cc = [[0, 1, 0],
      #       [0, 2, 0],              # Condições de Contorno [Nó, GL, Valor]
      #       [1, 1, 0],
      #       [1, 2, 0]]

      # Loads = [[2, 1, 1000]]       # Forças [Nó, GL, Valor]


      # Pré-Processamento (Cálculo do comprimento e rotação dos elementos)
      Vl, Vr = pre_proc(coord, conect, ne)

      # Processamento (Matriz de Rigidez Global e Vetor de Forças)
      K = matriz_rigidez(nn, ne, conect, VE, VA, Vl, Vr)

      F = forca(nn, Loads)

      Ka, Fa = cc_lagrange(nn, cc, K, F)
      Kf, Ff = cc_linha(nn, cc, K, F)

      Ua = np.linalg.solve(Ka, Fa)
      Ua2 = np.matmul(np.linalg.inv(Kf), Ff)

      U = Ua[0: 2*nn]

      # # Pós-Processamento (Cálculo dos Esforços e Tensões nos Elementos)
      # N = esforcos(ne, conect, VE, VA, Vl, Vr, U)

      # Sigma = []
      # for i in range(len(VA)):
      #       Sigma.append(N[i]/VA[i])

      # Plot dos resultados
      plot(coord, conect, ne, nn, U)


      return U, Ua2

U, Ua2 = main()

print(U)
print(Ua2)


