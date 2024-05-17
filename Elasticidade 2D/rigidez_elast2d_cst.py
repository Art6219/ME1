import numpy as np

from constitiva import constitutiva
from B_bi4n import B_bi4n

def rigidez_elast2d_cst(X, Y, esp, E, v, hip):

     # Monta a matriz constitutiva
     C = constitutiva(E, v, hip)

     # Calcula Matriz B
     x1 = X[0]
     x2 = X[1]
     x3 = X[2]

     y1 = Y[0]
     y2 = Y[1]
     y3 = Y[2]

     B = [[-(y3-y2)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0, (y3-y1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0, -(y2-y1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0],
          [0, (x3-x2)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0, -(x3-x1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), 0, (x2-x1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1)],
          [(x3-x2)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), -(y3-y2)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), -(x3-x1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), (y3-y1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), (x2-x1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1), -(y2-y1)/((x2-x1)*y3+(x1-x3)*y2+(x3-x2)*y1)]]

     # Calcula área do elemento triangular
     M = [[1, x1, y1],
          [1, x2, y2],
          [1, x3, y3]]

     A = 0.5 * np.linalg.det(M)

     # Calcula a matriz de rigidez do elemento
     K = np.linalg.multi_dot([B.transpose(), C, B])*A*esp

     return K