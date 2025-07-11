import numpy as np
from parametros import G

# Se calcula el producto matricial UxG
# Cada fila u[n] se multuplifca por G para producir la pal de codigo v[m]
def codificar(U):
    return np.mod(np.dot(U, G), 2) # aritmetica mod 2
