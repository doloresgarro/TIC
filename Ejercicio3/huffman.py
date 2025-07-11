import heapq

class NodoHuffman:
    def __init__(self, simbolo, prob, izq=None, der=None):
        self.simbolo = simbolo
        self.prob = prob
        self.izq = izq
        self.der = der
    def __lt__(self, otro):
        return self.prob < otro.prob

def construir_huffman(probabilidades):
    # se crea una lista de nodos inicial con su probabilidad
    heap = [NodoHuffman(simbolo, prob) for simbolo, prob in probabilidades.items()]
   
    # se convierte esa lista en una heap (cola de prioridades) -> nodo con menor priori queda 1ero
    heapq.heapify(heap)

    # se combinan los dos nodos menos probables hasta el fin del arbol 
    while len(heap) > 1:
        izq = heapq.heappop(heap)
        der = heapq.heappop(heap)
        nuevo = NodoHuffman(izq.simbolo + der.simbolo, izq.prob + der.prob, izq, der)
        heapq.heappush(heap, nuevo)
    
    arbol = heap[0]
    codigos = {}
    generar_codigos(arbol, '', codigos)
    return codigos

def generar_codigos(nodo, codigo, codigos):
    if nodo.izq is None and nodo.der is None:
        codigos[nodo.simbolo] = codigo
    else:
        generar_codigos(nodo.izq, codigo + '0', codigos)
        generar_codigos(nodo.der, codigo + '1', codigos)

