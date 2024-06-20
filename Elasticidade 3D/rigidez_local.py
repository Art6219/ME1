from rigidez_elast3d import rigidez_elast3d
from rigidez_elast3d_bolha import rigidez_elast3d_bolha
from rigidez_elast3d_cst import rigidez_elast3d_cst


def rigidez_local(ele_type, X, Y, Z, E, v, hip):

    # Matriz de Rigidez Local
    if ele_type == 1:
        Kl = rigidez_elast3d(X, Y, Z, E, v, hip)

    if ele_type == 2:
        Kl, _, _, _ = rigidez_elast3d_bolha(X, Y, Z, E, v, hip)
    else:
        pass

    
    return Kl