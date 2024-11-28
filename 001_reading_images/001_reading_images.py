

import os
import cv2
import matplotlib.pyplot as plt


print("Directorio de trabajo actual:", os.getcwd())
cb_img = cv2.imread("001_reading_images/checkerboard_18x18.png", 0)

print(cb_img)

# plt.imshow(cb_img)

plt.ion()  # Habilitar modo interactivo

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Gráfico en modo interactivo")
plt.show()

