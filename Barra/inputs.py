import numpy as np
import matplotlib.pyplot as plt

from main import main


# Seleciona qual problema será rodado
Problema = 1

# Lista dos problemas
if Problema == 1:
    
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


elif Problema == 2:
    
    # Inputs 2
    coord = [[0, 0],              # Coordenadas dos Pontos
                [1, 0],
                [0.5, np.sin(np.pi/3)]]

    conect = [[0, 2],             # Conectividades
                [1, 2]]

    E = 60e3                     # Módulo de Elasticidade
    A = 1                      # Área da Seção

    VE = E * np.ones(len(conect))
    VA = A * np.ones(len(conect))

    cc = [[0, 1, 0],
            [0, 2, 0],              # Condições de Contorno [Nó, GL, Valor]
            [1, 1, 0],
            [1, 2, 0]]

    Loads = [[2, 1, 1000]]       # Forças [Nó, GL, Valor]


# Chama a função main
Ua1, Ua2, Ua3, Sigma = main(coord, conect, Loads, cc, VE, VA)

print('Resolução por Lagrange')
print(Ua1)
print('------------------------------------------------------')
print('Resolução excluindo as linhas/colunas com restrições')
print(Ua2)
print('------------------------------------------------------')
print('Resolução zerando linhas/colunas com restrições')
print(Ua3)
print('------------------------------------------------------')
print('Tensões nos elementos')
print(Sigma)
print('------------------------------------------------------')

plt.show()