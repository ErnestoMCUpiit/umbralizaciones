import cv2  
import numpy as np
from bersem import bernsen
import matplotlib.pyplot as plt

celula = cv2.imread("image-cell.png", cv2.IMREAD_GRAYSCALE)
bacteria = cv2.imread("person_bacteria.jpeg", cv2.IMREAD_GRAYSCALE)
zebra = cv2.imread("zebra.jpg", cv2.IMREAD_GRAYSCALE)

imagen_umbralizada = bernsen(imagen_original, cmin=10, n=3, bg="oscuro")
plt.figure(figsize=(15, 5))

plt.subplot(331) 
plt.imshow(celula)
plt.title('original')

plt.subplot(332)  
plt.imshow(cv2.cvtColor(imagen2, cv2.COLOR_BGR2RGB))
plt.title('Global')

plt.subplot(333)  
plt.imshow(cv2.cvtColor(imagen3, cv2.COLOR_BGR2RGB))
plt.title('Otsu')

plt.subplot(334)
plt.imshow(bernsen(celula, cmin=10, n=3, bg="claro"))
plt.title('local adaptativa por el método de Bernsen')

cv2.imshow("imagen_umbralizada", imagen_umbralizada)
cv2.waitKey(0)
cv2.destroyAllWindows()