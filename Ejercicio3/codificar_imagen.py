
def codificar_secuencia(secuencia, codigos, orden):
    mensajes = [''.join(map(str, secuencia[i:i+orden])) for i in range(len(secuencia) - orden + 1)]
    
    # Se busca para c/ mensaje su cod de Huffman en el diccionario
    codificada = ''.join([codigos[mensaje] for mensaje in mensajes])
    
    return codificada
