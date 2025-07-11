import numpy as np
from parametros import H
# np.dot -> calcula el producto matricial (param -> 2: indica aritmetica binaria)

def detectar(Vr, U_original):
    # si  s = 0 -> no hay error
    #     s distinto 0 -> hay error y coincide con una de las filas de H^t
    
    Ht = H.T
    V_corr = []
    U_filtrados = []
    for i in range(Vr.shape[0]):
        s = np.mod(np.dot(Vr[i].flatten(), Ht), 2) # se calcula s para c/ palabra
        print(f"Palabra {i}: síndrome = {s}")  # imprime el síndrome
        if not np.all(s == 0):
            # hay error
            print(f"Error detectado en la palabra {i}, se descarta.")

        else:
            # no hay error
            print(f"Palabra {i}: sin errores")
            V_corr.append(Vr[i])
            U_filtrados.append(U_original[i])

    if len(V_corr) == 0:
        print("Todas las palabras fueron descartadas, no hay datos para decodificar.")
        return np.zeros((0, Vr.shape[1]), dtype=int), np.zeros((0, U_original.shape[1]), dtype=int), len(Vr)

    V_corr = np.array(V_corr)
    U_filtrados = np.array(U_filtrados)

    return V_corr, U_filtrados, len(Vr) - len(V_corr) 
# devuelve también cuántas palabras fueron descartadas 

