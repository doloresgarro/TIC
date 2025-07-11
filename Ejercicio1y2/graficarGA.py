import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfcinv

def graficar_ganancia_asintotica(EbN0_dB_range, Pe_b_values, Ga):
    Pe_b_simulado = np.array(Pe_b_values)
    EbN0_con_cod = np.array(EbN0_dB_range)

    M = 10000
    minimo = 1/M
    Pe_b_simulado = np.clip(Pe_b_simulado, minimo, 1)

    with np.errstate(divide='ignore', invalid='ignore'):
        EbN0_teorico_sin_cod_linear = (erfcinv(2 * Pe_b_simulado)) ** 2
        EbN0_teorico_sin_cod_dB = 10 * np.log10(EbN0_teorico_sin_cod_linear)

    Ganancia_real_codigo = EbN0_teorico_sin_cod_dB - EbN0_con_cod
    Ganancia_real_codigo = np.where(np.isfinite(Ganancia_real_codigo), Ganancia_real_codigo, np.nan)

    #plt.figure()
    plt.figure(figsize=(10,5))
    plt.plot(EbN0_con_cod, Ganancia_real_codigo, 'o-', label='Ganancia real del código')
    plt.axhline(y=Ga, color='k', linestyle='--', label=f'Ga (asintótica) = {Ga:.2f} dB')
    plt.xlabel('Eb/N0 (dB)')
    plt.ylabel('Ganancia (dB)')
    plt.title('Ganancia asintótica vs Ganancia real del código')
    plt.grid(True, which='both')
    plt.legend()
    plt.show()
