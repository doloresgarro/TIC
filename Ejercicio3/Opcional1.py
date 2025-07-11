from leer_imagen import leer_imagen
from calcular_probabilidades import calcular_probabilidades
from huffman import construir_huffman
from codificar_imagen import codificar_secuencia
from calculos import calcular_largo_promedio, calcular_tasa_compresion
import matplotlib.pyplot as plt

secuencia, shape = leer_imagen('C:\\Users\\Dolores\\Documents\\Facultad\\Teoría de la información y la codificación\\Laboratorio\\Laboratorio TIC\\Ejercicio3\\logo FI.tif')

# Opcional 1:Automatice el algoritmo de codificaci´on para fuente extendida de orden n y releve la curva Largo promedio vs. n.
rangos_n = range(1, 7)
valores_L = []

for orden in rangos_n:
    print(f"\n Fuente extendida de orden {orden}")
    probabilidades, conteo = calcular_probabilidades(secuencia, orden)
    #print("Probabilidades:", probabilidades)

    codigos = construir_huffman(probabilidades)
    #print("Códigos Huffman:", codigos)

    #codificada = codificar_secuencia(secuencia, codigos, orden)
    L = calcular_largo_promedio(probabilidades, codigos)
    #tasa = calcular_tasa_compresion(secuencia, codificada)
    
    print(f"Largo promedio: {L:.3f}")
    #print(f"Tasa de compresión: {tasa:.3f}")

    valores_L.append(L)


# PRUEBAS
print(f"SUMA PROBAS: {sum(probabilidades.values()):.3f}\n")


# Graficar L vs n
plt.figure(figsize=(8,5))
plt.plot(list(rangos_n), valores_L, marker='o', linestyle='-')
plt.xlabel('Orden n de la fuente extendida')
plt.ylabel('Largo promedio L')
plt.title('Curva Largo promedio L vs. n')
plt.grid(True)
plt.show()
