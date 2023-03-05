import cv2
import numpy as np

# Load beberapa citra yang ingin dirata-ratakan
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpg')
img3 = cv2.imread('3.jpg')

# Konversi citra ke dalam skala keabuan
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray_img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

# Gabungkan citra-citra tersebut ke dalam sebuah array
images = np.array([gray_img1, gray_img2, gray_img3])

# Hitung rata-rata dari array tersebut
average_img = np.average(images, axis=0)

# Konversi hasil rata-rata ke dalam tipe data yang sama dengan citra input
average_img = average_img.astype(np.uint8)

# Tampilkan hasil
cv2.imshow('Averaged Image', average_img)
cv2.waitKey(0)
cv2.destroyAllWindows()