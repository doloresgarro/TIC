from PIL import Image
import numpy as np

def leer_imagen(imagen):
    # Cargar la imagen
    img = Image.open(imagen).convert('L')           # transforma imagen a escala de grises
    img_array = np.array(img)                       # matriz con valores de intesidad por pixel -> 0 = negro, 255 = blanco

    # Convertir a binario: blanco = 1, negro = 0
    binaria = (img_array > 128).astype(int)         # true si es + claro que 128, sino false
                                                    # astype(int) -> convierte true/false a 1/0
    
    # Colocar elementos en un unico vector
    secuencia = binaria.flatten()
    
    return secuencia, binaria.shape
