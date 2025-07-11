def calcular_largo_promedio(probabilidades, codigos):
    return sum(prob * len(codigos[mensaje]) for mensaje, prob in probabilidades.items())

def calcular_tasa_compresion(secuencia, codificada):
    largo_original = len(secuencia)  # bits sin codificar
    largo_codificado = len(codificada)
    return largo_original / largo_codificado
