import cv2  
import numpy as np
from bersem import bernsen
import matplotlib.pyplot as plt

celula = cv2.imread("image-cell.png", cv2.IMREAD_GRAYSCALE)
bacteria = cv2.imread("person_bacteria.jpeg", cv2.IMREAD_GRAYSCALE)
zebra = cv2.imread("zebra.jpg", cv2.IMREAD_GRAYSCALE)

bersen1 = bernsen(celula, cmin=20, n=11, bg="claro")
bersen2 = bernsen(bacteria, cmin=10, n=3, bg="oscuro")
bersen3 = bernsen(zebra, cmin=10, n=3, bg="oscuro")

plt.figure(figsize=(15, 5))

# imagenes procesadas celula
plt.subplot(341) 
plt.imshow(celula)
plt.title('original')

plt.subplot(342)  
plt.imshow(celula)
plt.title('Global')

plt.subplot(343)  
plt.imshow(celula)
plt.title('Otsu')

plt.subplot(344)
plt.imshow(bersen1,cmap="gray")
plt.title('local adaptativa por el método de Bernsen')

#imagenes procesadas bacteria
plt.subplot(345) 
plt.imshow(bacteria)
plt.title('original')

plt.subplot(346)  
plt.imshow(bacteria)
plt.title('Global')

plt.subplot(347)  
plt.imshow(bacteria)
plt.title('Otsu')

plt.subplot(348)
plt.imshow(bersen2,cmap="gray")
plt.title('local adaptativa por el método de Bernsen')

#imagenes procesadas paso de cebra
plt.subplot(349) 
plt.imshow(zebra)
plt.title('original')

plt.subplot(3,4 ,10)  
plt.imshow(zebra)
plt.title('Global')

plt.subplot(3,4,11)  
plt.imshow(zebra)
plt.title('Otsu')

plt.subplot(3,4,12)
plt.imshow(bersen3, cmap="gray")
plt.title('local adaptativa por el método de Bernsen')

plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()