import cv2
import numpy as np
import matplotlib.pyplot as plt




image = cv2.imread('forcanny.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Ошибка: не удалось загрузить изображение.")
else:

    edges_canny = cv2.Canny(image, 100, 200)

   
    cv2.imshow("Original", image)
    cv2.imshow("Canny Edges", edges_canny)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
