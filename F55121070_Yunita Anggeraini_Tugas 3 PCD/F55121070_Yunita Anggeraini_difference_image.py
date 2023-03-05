import cv2
import numpy as np

# Load dua buah citra yang ingin dibandingkan
img1 = cv2.imread('img1.jpg')
img2 = cv2.imread('img2.jpg')

# Ubah citra ke dalam skala keabuan
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Hitung perbedaan antara kedua citra
diff_img = cv2.absdiff(gray_img1, gray_img2)

# Lakukan histogram equalization pada difference image
eq_diff_img = cv2.equalizeHist(diff_img)

# Tampilkan hasil
cv2.imshow('Difference Image', diff_img)
cv2.imshow('Histogram Equalization Difference Image', eq_diff_img)
cv2.waitKey(0)
cv2.destroyAllWindows()