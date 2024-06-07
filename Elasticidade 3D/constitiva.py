def constitutiva(E, v, hip):

    G = E/(2*(1 + v))       # Módulo de Elasticidade Transversal
    
    if hip == 'EPT':        # Estado plano de tensão
        
        a = E/(1 - v**2)

        C = [[a, v*a, 0],
             [v*a, a, 0],
             [0, 0, G]]

    elif hip == 'EPD':      # Estado plano de deformação

        d = (v + 1)*(2*v - 1)  
        a = E*(v - 1)/d
        b = -(E*v)/d

        C = [[a, b, 0],
             [b, a, 0],
             [0, 0, G]]
        
    elif hip == '3D':       # Estado 3D

        a = 1/E
        b = v/E
        G = 2*E*(1 + v)
        
        C = [[a, b, b, 0, 0, 0],
             [b, a, b, 0, 0, 0],
             [b, b, a, 0, 0, 0],
             [0, 0, 0, G, 0, 0],
             [0, 0, 0, 0, G, 0],
             [0, 0, 0, 0, 0, G]]
        
    return C
    
