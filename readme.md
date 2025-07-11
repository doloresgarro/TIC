# Trabajo Práctico de Simulación - Teoría de la Información y Codificación

Este repositorio contiene la implementación de un sistema de comunicación digital con codificación de canal y de fuente, desarrollado para la materia **Teoría de la Información y Codificación** (2025), en el marco de la carrera de Ingeniería en Computación.

## 📌 Objetivos

- Simular un sistema de comunicación digital sobre un canal AWGN utilizando codificación de canal.
- Evaluar el desempeño del sistema con y sin codificación, en términos de tasa de error de bit y de palabra.
- Implementar compresión de datos mediante el algoritmo de Huffman sobre una imagen binaria.
- Validar los resultados teóricos con simulaciones.

---

## 🛰️ Parte 1: Codificación de Canal

Se implementó un esquema de transmisión digital que incluye codificación de canal utilizando un **código lineal de bloque (14,10)**. El sistema simulado incluye las siguientes etapas:

- **Codificación**: Se generan bloques de 10 bits que se codifican a 14 bits mediante una matriz generadora sistemática.
- **Modulación BPSK**: Se modula la secuencia binaria y se transmite sobre un canal con ruido blanco aditivo gaussiano (AWGN).
- **Transmisión con ruido**: Se varía la relación señal-ruido (Eb/N0) para evaluar el rendimiento del sistema.
- **Detección y corrección**: Se utiliza detección dura y cálculo del síndrome para corregir errores simples.
- **Decodificación**: Se recupera el mensaje original a partir de los bits de información.

### Resultados

- Se graficaron las curvas de **tasa de error de bit (Peb)** y **tasa de error de palabra (Pep)** en función de Eb/N0.
- Se compararon los resultados obtenidos con los valores teóricos.
- Se calculó la **ganancia asintótica de codificación**, obteniendo un valor cercano a **1.43 dB**, lo cual valida la efectividad del esquema implementado.

---

## 📦 Parte 2: Codificación de Fuente

Se utilizó el **algoritmo de Huffman** para comprimir la imagen binaria `logoFI.tif` (provista por la cátedra).

### Etapas

- La imagen se convirtió a binario aplicando un umbral (valores > 128 considerados blancos).
- Se construyeron fuentes extendidas de **orden 2 y 3**, evaluando las frecuencias relativas de aparición de cada bloque.
- Se generó el árbol de Huffman para cada caso y se codificó la secuencia.
- Se calcularon las métricas de eficiencia:
  - **Largo promedio de código**.
  - **Tasa de compresión lograda**.
  ---

## 🛠️ Herramientas utilizadas

- **Lenguaje:** Python
- **Librerías:** NumPy, Matplotlib, PIL (para manipulación de imágenes)
- Se optó por Python por su versatilidad para simulaciones matemáticas y manipulación de datos.

---