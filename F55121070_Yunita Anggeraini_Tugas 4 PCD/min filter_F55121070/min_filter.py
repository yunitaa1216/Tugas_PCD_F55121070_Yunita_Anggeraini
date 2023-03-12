#Yunita Anggeraini
#F55121070
import cv2
import numpy as np

# membaca gambar
img = cv2.imread('Noise1.jpg')

# konversi gambar menjadi grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# membuat kernel 5x5
kernel = np.ones((5,5),np.uint8)

# melakukan erosi dengan kernel 5x5
min_filter = cv2.erode(gray, kernel, iterations = 1)

# menampilkan gambar asli dan hasil min filter
cv2.imshow('Original Image', gray)
cv2.imshow('Min Filter', min_filter)

# menunggu tombol keyboard ditekan
cv2.waitKey(0)

# menutup semua jendela
cv2.destroyAllWindows()