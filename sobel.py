import cv2
import numpy as np


image_path = "forsobel.jpg"  


image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Ошибка: не удалось загрузить изображение.")
else:
  
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  
    sobel_combined = cv2.magnitude(sobelx, sobely)  

   
    sobel_combined = np.uint8(sobel_combined)

   
    cv2.imshow("Original", image)
    cv2.imshow("Sobel Combined", sobel_combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
