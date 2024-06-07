from rigidez_elast2d import rigidez_elast2d
from rigidez_elast2d_bolha import rigidez_elast2d_bolha
from rigidez_elast2d_cst import rigidez_elast2d_cst


def rigidez_local(ele_type, X, Y, esp, E, v, hip):

    # Matriz de Rigidez Local
    if ele_type == 1:
        Kl = rigidez_elast2d(X, Y, esp, E, v, hip)
    elif ele_type == 2:
        Kl = rigidez_elast2d_bolha(X, Y, esp, E, v, hip)
    elif ele_type == 3:
        Kl = rigidez_elast2d_cst(X, Y, esp, E, v, hip)

    
    return Kl