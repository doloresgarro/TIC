from leer_imagen import leer_imagen
from calcular_probabilidades import calcular_probabilidades
from huffman import construir_huffman
from codificar_imagen import codificar_secuencia
from calculos import calcular_largo_promedio, calcular_tasa_compresion

secuencia, shape = leer_imagen('C:\\Users\\Dolores\\Documents\\Facultad\\Teoría de la información y la codificación\\Laboratorio\\Laboratorio TIC\\Ejercicio3\\logo FI.tif')

for orden in [2, 3]:
    print(f"\n Fuente extendida de orden {orden}")
    probabilidades, conteo = calcular_probabilidades(secuencia, orden)
    print("Probabilidades:", probabilidades)

    codigos = construir_huffman(probabilidades)
    print("Códigos Huffman:", codigos)

    codificada = codificar_secuencia(secuencia, codigos, orden)
    L = calcular_largo_promedio(probabilidades, codigos)
    tasa = calcular_tasa_compresion(secuencia, codificada)
    
    print(f"Largo promedio: {L:.3f}")
    print(f"Tasa de compresión: {tasa:.3f}")


# PRUEBAS
print(f"SUMA PROBAS: {sum(probabilidades.values()):.3f}\n")


for simbolo, codigo in codigos.items():
    print(f"Símbolo: {simbolo}, Código: {codigo}, Longitud: {len(codigo)}")

for simbolo, prob in sorted(probabilidades.items(), key=lambda x: -x[1]):
    print(f"Símbolo: {simbolo}, Probabilidad: {prob:.3f}, Código: {codigos[simbolo]}")

import math
H = -sum(prob * math.log2(prob) for prob in probabilidades.values())
print(f"Entropía H: {H:.3f}, Largo promedio L: {L:.3f}")
