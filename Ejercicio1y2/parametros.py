# Script en donde armo la matriz generadora G y H transpuesta
import numpy as np

k = 10                  # long de mensaje 
n = 14                  # long de palabra de código
I = np.identity(k, dtype=int) # matriz identidad de kxk = 10x10

# Defino matriz de paridad --> P [kx(n-k)]
P = np.array([
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1],
    [1,0,1,1],
    [1,1,0,1],
    [1,1,1,0],
    [0,1,1,1],
    [1,1,1,1],
    [0,1,0,1],
])
G = np.concatenate((I, P), axis = 1)
H = np.concatenate((P.T, np.identity(n-k, dtype=int)), axis = 1)
