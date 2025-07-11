import numpy as np
from parametros import k, n

def canal_bpsk_awgn(V, EbN0_dB):
    A = 1                               # Amplitud señal
    Es = A**2                           # energía de simb de canal
    Ebf = Es * (n/k)                    #
    EbN0 = 10**(EbN0_dB/10)             # en veces 
    N0 = Ebf / EbN0                     

    ruido = np.sqrt(N0/2) * np.random.randn(*V.shape) # ruido real
    s = (2 * V - 1) * A                               # modulacion BPSK
    r = s + ruido
    Vr = (r > 0).astype(int)                          # deteccion dura
    return Vr
