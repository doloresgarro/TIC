from collections import Counter

def calcular_probabilidades(secuencia, orden):
    mensajes = []

    # Se recorre secuencia con bloques de longitud "orden" (2 o 3)
    for i in range(len(secuencia) - orden + 1):
        mensaje = ''.join(map(str, secuencia[i:i+orden]))  
        mensajes.append(mensaje)

    total = len(mensajes)           # cant total de bloques generador
    conteo = Counter(mensajes)      # cuenta cant de veces que aparece c/ bloque

    # Se calcula las probabilidades de cada bloque 
    probabilidades = {mensaje: conteo[mensaje]/total for mensaje in conteo} 
    
    return probabilidades, conteo
