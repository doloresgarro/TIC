# Programa principal
from matplotlib import pyplot as plt
import numpy as np
from codificador import codificar
from canalCSB import canal_bpsk_awgn
from deteccion_y_correccion import detectar_corregir
from decodificador import decodificar
from errores import calcular_errores
from parametros import H, k, n
from gananciaAsintotica import calcular_gananciaAsintotica
from graficar import graficar_teorico_bpsk, graficar_codificacion
from deteccion import detectar
from graficarGA import graficar_ganancia_asintotica

np.random.seed(None)

M = 10    # cantidad de palabras1 de código -> 1000 msj
#EbN0_dB_range = np.arange(-2, 10, 1)   # relacion señal/ruido -> cuanto menor es, mas errores hay ->  Peb y Pep aumentan
#EbN0_dB_range = np.arange(-10, 2, 1)   # va desde -10 dB a 2 dB con paso 1
EbN0_dB_range = np.arange(-2, 31, 1)    # prueba para corrector
#EbN0_dB_range =np.arange(-2, 10, 1)    # prueba para detector
Pe_b_values = []
Pe_p_values = []

# Se solicita elegir detector-corrector o detector
modo = input("Seleccionar modo:\n1 - detector1 y corrector (1)\n2 - Solo detector (2)\nOpción: ")

for EbN0_dB in EbN0_dB_range: 
    # Se generan M mensajes aleatorios
    U = np.random.randint(0, 2, size=(M, k))            # se generan M msjs aleatorios de long k bits -> u[n]
    #print("Mensajes originales:\n", U)

    # Codificación
    V = codificar(U)                                    # u*G

    # Canal BPSK con ruido
    Vr = canal_bpsk_awgn(V, EbN0_dB)                    # bits de v[m] se modulan en BPSK y se trasmite por canal con RG

    # Detección y correción de errores
    if (modo == "1"):
        V_corr = detectar_corregir(Vr)                  # se calcula sindrome y si hay error se corrige
        # Decodificación 
        U_hat = decodificar(V_corr)                     # se recupera el mensaje tomando los 1eros k bits
        #print("Mensajes recuperados:\n", U_hat)

         # Se calculan errores
        Pe_b, Pe_p = calcular_errores(U, U_hat)         # se calculan probabilidades de error de bit y de palabra
        print(f"Pe_b: {Pe_b:.6f}, Pe_p: {Pe_p:.6f}")   
    
    else:   
        
        V_corr, U_filtrados, num_descartadas = detectar(Vr, U)

        if V_corr.shape[0] == 0:
            print(f"Eb/N0={EbN0_dB} dB: todas las palabras fueron descartadas.")
            Pe_b = 1.0  
            Pe_p = 1.0
        else:
            
            U_hat = decodificar(V_corr)

            total_bits = U.shape[0] * U.shape[1]
            total_palabras = U.shape[0]

            errores_bits = num_descartadas * k + np.sum(U_filtrados != U_hat)
            errores_palabras = num_descartadas + np.sum(np.any(U_filtrados != U_hat, axis=1))

            Pe_b = errores_bits / total_bits
            Pe_p = errores_palabras / total_palabras
              

    # Se almacena valor de Peb o Pep para c/ punto de Eb/N0
    Pe_b_values.append(Pe_b)
    Pe_p_values.append(Pe_p)
    print(f"Eb/N0={EbN0_dB} dB: Pe_b={Pe_b:.6f}, Pe_p={Pe_p:.6f}")

# Se crean los gráficos
graficar_codificacion(EbN0_dB_range, Pe_b_values, Pe_p_values)
graficar_teorico_bpsk(EbN0_dB_range)

plt.xlabel('Eb/N0 (dB)')
plt.ylabel('Probabilidad de error')
plt.title('Curvas de error vs Eb/N0')
plt.grid(True, which='both')
plt.legend()
plt.show()


# Se calcula Ga
Ga = calcular_gananciaAsintotica()
print(f"Ganancia de codificación asintótica (Ga): {Ga:.3f}")
graficar_ganancia_asintotica(EbN0_dB_range, Pe_b_values, Ga)