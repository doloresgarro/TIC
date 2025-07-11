import numpy as np

def calcular_errores(U_original, U_recuperado):
    errores_bits = np.sum(U_original != U_recuperado)
    total_bits = U_original.size
    errores_palabras = np.sum(np.any(U_original != U_recuperado, axis=1))
    total_palabras = U_original.shape[0]
    Pe_b = errores_bits / total_bits
    Pe_p = errores_palabras / total_palabras
    return Pe_b, Pe_p
