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

      # Processamento (Matriz de Rigidez Global, Vetor de Forças e Vetor de Deslocamentos)
      K = matriz_rigidez(nn, ne, conect, VE, VA, Vl, Vr)

      F = forca(nn, Loads)

      Ka, Fa = cc_lagrange(nn, cc, K, F)
      Ua = np.linalg.solve(Ka, Fa)
      Ua1 = Ua[0: 2*nn]

      Kf, Ff = cc_exc_linha(nn, cc, K, F)
      Ua2 = np.matmul(np.linalg.inv(Kf), Ff)

      Kn, Fn = cc_1_linha(nn, cc, K, F)
      Ua3 = np.matmul(np.linalg.inv(Kn), Fn)

      # Pós-Processamento (Cálculo dos Esforços e Tensões nos Elementos)
      N = esforcos(ne, conect, VE, VA, Vl, Vr, Ua1)

      Sigma = []
      for i in range(len(VA)):
            Sigma.append(N[i]/VA[i])

      # Plot dos resultados
      plot(coord, conect, ne, nn, Ua1)


      return Ua1, Ua2, Ua3


Ua1, Ua2, Ua3 = main()

print('Resolução por Lagrange')
print(Ua1)
print('------------------------------------------------------')
print('Resolução excluindo as linhas/colunas com restrições')
print(Ua2)
print('------------------------------------------------------')
print('Resolução zerando linhas/colunas com restrições')
print(Ua3)
print('------------------------------------------------------')

plt.show()


