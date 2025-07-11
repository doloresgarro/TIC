import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

def graficar_teorico_bpsk(EbN0_dB_range):
    EbN0_linear = 10**(EbN0_dB_range/10)
    Pe_b_teorico = 0.5 * erfc(np.sqrt(EbN0_linear))
    plt.semilogy(EbN0_dB_range, Pe_b_teorico, 'x-', label='Pe_b (teórico sin cod)', linewidth=0.8, markersize=4)

def graficar_codificacion(EbN0_dB_range, Pe_b_values, Pe_p_values):
    plt.figure()
    plt.semilogy(EbN0_dB_range, Pe_b_values, 'o-', label='Pe_b (con codificación)', linewidth=0.8, markersize=4)
    plt.semilogy(EbN0_dB_range, Pe_p_values, 's-', label='Pe_p (con codificación)', linewidth=0.8, markersize=4)
