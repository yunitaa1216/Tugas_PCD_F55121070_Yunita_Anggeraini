#Yunita Anggeraini
#F55121070
import cv2
import numpy as np

# Load gambar asli
img = cv2.imread('tes.jpg', cv2.IMREAD_GRAYSCALE)

# Tentukan ukuran kernel
kernel_size = 5

# Buat kernel max filter
kernel = np.ones((kernel_size, kernel_size), np.uint8)

# Lakukan operasi max filter
max_filter = cv2.dilate(img, kernel)

# Tampilkan gambar asli dan hasil max filter
cv2.imshow('Gambar Asli', img)
cv2.imshow('Hasil Max Filter', max_filter)

# Tunggu tombol key ditekan
cv2.waitKey(0)
cv2.destroyAllWindows()