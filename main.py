import cv2  # Asegúrate de tener OpenCV instalado
import numpy as np
from bersem import bernsen
import matplotlib.pyplot as plt

# Cargar la imagen
imagen_original = cv2.imread("imagen.png", cv2.IMREAD_GRAYSCALE)

# Aplicar el algoritmo de umbralización de Berntsen
imagen_umbralizada = bernsen(imagen_original, cmin=10, n=3, bg="oscuro")

# Guardar la imagen umbralizada
cv2.imshow("imagen_umbralizada", imagen_umbralizada)
cv2.waitKey(0)
cv2.destroyAllWindows()