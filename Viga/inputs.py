import numpy as np
import matplotlib.pyplot as plt

from main import main


# Seleciona qual problema será rodado
Problema = "Trabalho_10_el"

# Lista dos problemas
if Problema == 1:
    
    # Inputs 1
    coord = [[0, 0],
             [1, 0],              
             [2, 0]]             # Coordenadas dos Pontos

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

    Loads = [[2, 3, 50]]       # Forças [Nó, GL, Valor]

    Load_dist = [[1, 10, 10]]   # Forças distribuidas [Elemento, q1, q2]


elif Problema == "Trabalho_Original":

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

    E = 150e9                     # Módulo de Elasticidade
    D = 0.05
    A = np.pi * D**2 / 4                      # Área da Seção
    I = np.pi * D**4 / 64                    # Momento de Inércia da Seção

    VE = E * np.ones(ne)
    VA = A * np.ones(ne)
    VI = I * np.ones(ne)

    cc = [[0, 1, 0],              # Condições de Contorno [Nó, GL, Valor]
          [0, 2, 0],
          [1, 2, 0]]

    Loads = [[3, 3, 500]]       # Forças [Nó, GL, Valor]

    Load_dist = [[2, -500, -800]]   # Forças distribuidas [Elemento, q1, q2]


elif Problema == "Trabalho_teste":

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

    E = 150e9                     # Módulo de Elasticidade
    D = 0.05
    A = np.pi * D**2 / 4                      # Área da Seção
    I = np.pi * D**4 / 64                    # Momento de Inércia da Seção

    VE = E * np.ones(ne)
    VA = A * np.ones(ne)
    VI = I * np.ones(ne)

    cc = [[0, 1, 0],              # Condições de Contorno [Nó, GL, Valor]
          [0, 2, 0],
          [1, 2, 0]]

    Loads = [[3, 3, 500]]       # Forças [Nó, GL, Valor]

    Load_dist = [[2, -500, -800]]   # Forças distribuidas [Elemento, q1, q2]


elif Problema == "Trabalho_2_el":

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

    E = 150e9                     # Módulo de Elasticidade
    D = 0.05
    A = np.pi * D**2 / 4                      # Área da Seção
    I = np.pi * D**4 / 64                    # Momento de Inércia da Seção

    VE = E * np.ones(ne)
    VA = A * np.ones(ne)
    VI = I * np.ones(ne)

    cc = [[0, 1, 0],              # Condições de Contorno [Nó, GL, Valor]
          [0, 2, 0],
          [1, 2, 0]]

    Loads = [[3, 3, 500]]       # Forças [Nó, GL, Valor]

    Load_dist = [[2, -500, -800]]   # Forças distribuidas [Elemento, q1, q2]
    

elif Problema == "Trabalho_10_el":

    # Inputs 1
    coord = [[0, 0],              # Coordenadas dos Pontos
             [1, 0],
             [2, 0],
             [2.1, 0.17320508075688773], 
            [2.2, 0.34641016151377546], 
            [2.3, 0.5196152422706632], 
            [2.4, 0.6928203230275509], 
            [2.5, 0.8660254037844386], 
            [2.6, 1.0392304845413265], 
            [2.7, 1.2124355652982142], 
            [2.8, 1.3856406460551018], 
            [2.9, 1.5588457268119895], 
            [3.0, 1.7320508075688772]]

    conect = [[0, 1],            # Conectividades
              [1, 2],
              [2, 3],
              [3, 4],
              [4, 5],
              [5, 6],
              [6, 7],
              [7, 8],
              [8, 9],
              [9, 10],
              [10, 11],
              [11, 12]]             

    nn = len(coord)               # Número de Nós
    ne = len(conect)              # Número de Elementos

    E = 150e9                     # Módulo de Elasticidade
    D = 0.05
    A = np.pi * D**2 / 4                      # Área da Seção
    I = np.pi * D**4 / 64                    # Momento de Inércia da Seção

    VE = E * np.ones(ne)
    VA = A * np.ones(ne)
    VI = I * np.ones(ne)

    cc = [[0, 1, 0],              # Condições de Contorno [Nó, GL, Valor]
          [0, 2, 0],
          [1, 2, 0]]

    Loads = [[12, 3, 500]]       # Forças [Nó, GL, Valor]

    Load_dist = [[2, -500.0, -530.0], 
                 [3, -530.0, -560.0], 
                 [4, -560.0, -590.0], 
                 [5, -590.0, -620.0], 
                 [6, -620.0, -650.0], 
                 [7, -650.0, -680.0], 
                 [8, -680.0, -710.0], 
                 [9, -710.0, -740.0], 
                 [10, -740.0, -770.0], 
                 [11, -770.0, -800.0]]   # Forças distribuidas [Elemento, q1, q2]


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