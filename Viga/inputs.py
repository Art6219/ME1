import numpy as np
import matplotlib.pyplot as plt

from main import main


# Seleciona qual problema será rodado
Problema = 1

# Lista dos problemas
if Problema == 1:
    
    # Inputs 1
    coord = [[0, 0],              # Coordenadas dos Pontos
            [0, 1],
            [1, 1]]

    conect = [[0, 1],            # Conectividades
              [1, 2]]             

    nn = len(coord)               # Número de Nós
    ne = len(conect)              # Número de Elementos

    E = 100e3                     # Módulo de Elasticidade
    A = 1                      # Área da Seção
    I = 1e-4                    # Momento de Inércia da Seção

    VE = E * np.ones(ne)
    VA = A * np.ones(ne)
    VI = I * np.ones(ne)

    cc = [[0, 1, 0],              # Condições de Contorno [Nó, GL, Valor]
        [0, 2, 0],
        [0, 3, 0]]

    Loads = [[2, 2, 0.5]]       # Forças [Nó, GL, Valor]

    Load_dist = [[0, 0, 0]]   # Forças distribuidas [Elemento, q1, q2]


elif Problema == 2:

    pass
    

# Chama a função main
Ua1, Ua2, Ua3, Sigma = main(coord, conect, Loads, Load_dist, cc, VE, VA, VI)

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