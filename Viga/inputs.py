import numpy as np
import matplotlib.pyplot as plt

from main import main


# Seleciona qual problema será rodado
Problema = 1

# Lista dos problemas
if Problema == 1:
    
    # Inputs 1
    coord = [[0, 0],
             [0.5, 0],              
             [1, 0]]             # Coordenadas dos Pontos

    conect = [[0, 1],
              [1, 2]]           # Conectividades            
                 

    nn = len(coord)               # Número de Nós
    ne = len(conect)              # Número de Elementos

    # A = np.pi*0.012**2
    # I = np.pi*0.012**4/64
    E = 100e9                     # Módulo de Elasticidade
    A = 5e-4                      # Área da Seção
    I = 5e-10                    # Momento de Inércia da Seção

    VE = E * np.ones(ne)
    VA = A * np.ones(ne)
    VI = I * np.ones(ne)

    cc = [[0, 1, 0],              
         [0, 2, 0],
         [0, 3, 0]]              # Condições de Contorno [Nó, GL, Valor]

    Loads = [[2, 2, -100],
             [1, 2, -125]]       # Forças [Nó, GL, Valor]

    Load_dist = [[0, 0, 0]]   # Forças distribuidas [Elemento, q1, q2]


elif Problema == "Trabalho":

    # Inputs 1
    coord = [[0, 0],              # Coordenadas dos Pontos
             [1, 0],
             [2, 0],
             [2+2*np.cos(np.pi/3), 2*np.sin(np.pi/3)]]

    conect = [[0, 1],            # Conectividades
              [1, 2],
              [2, 3]]             

    nn = len(coord)               # Número de Nós
    ne = len(conect)              # Número de Elementos

    E = 50e9                     # Módulo de Elasticidade
    A = 5e-4                      # Área da Seção
    I = 5e-10                    # Momento de Inércia da Seção

    VE = E * np.ones(ne)
    VA = A * np.ones(ne)
    VI = I * np.ones(ne)

    cc = [[0, 1, 0],              # Condições de Contorno [Nó, GL, Valor]
          [0, 2, 0],
          [1, 2, 0]]

    Loads = [[3, 3, -3]]       # Forças [Nó, GL, Valor]

    Load_dist = [[2, 2, 4]]   # Forças distribuidas [Elemento, q1, q2]


# Chama a função main
Ua1, Ua2, Ua3, Sigma = main(coord, conect, Loads, Load_dist, cc, VE, VA, VI)

print('Resolução por Lagrange')
print(Ua1)
# print('------------------------------------------------------')
# print('Resolução excluindo as linhas/colunas com restrições')
# print(Ua2)
# print('------------------------------------------------------')
# print('Resolução zerando linhas/colunas com restrições')
# print(Ua3)
print('------------------------------------------------------')
print('Tensões nos elementos')
print(Sigma)
print('------------------------------------------------------')

plt.show()