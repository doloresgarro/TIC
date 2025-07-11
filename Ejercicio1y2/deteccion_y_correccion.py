import numpy as np
from parametros import H
# np.dot -> calcula el producto matricial (param -> 2: indica aritmetica binaria)

def detectar_corregir(Vr):
    # si  s = 0 -> no hay error
    #     s distinto 0 -> hay error y coincide con una de las filas de H^t
    
    Ht = H.T
    V_corr = Vr.copy()
    for i in range(Vr.shape[0]):
        s = np.mod(np.dot(Vr[i].flatten(), Ht), 2) # se calcula s para c/ palabra
        print(f"Palabra {i}: síndrome = {s}")  # imprime el síndrome
        if not np.all(s == 0):
            # hay error
            for j in range(Ht.shape[0]):
                if np.array_equal(s, Ht[j]):
                        V_corr[i,j] ^= 1          # invierto el bit errado
                        print(f"Error corregido en bit {j} de la palabra {i}")
                        break
        else:
            # no hay error
            print(f"Palabra {i}: sin errores")

    return V_corr


