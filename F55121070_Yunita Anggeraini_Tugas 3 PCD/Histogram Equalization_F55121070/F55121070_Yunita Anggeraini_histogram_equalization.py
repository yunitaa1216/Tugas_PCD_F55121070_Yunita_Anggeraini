import cv2
import matplotlib.pyplot as plt

# Baca gambar dengan kontras rendah
img_low_contrast = cv2.imread('rendah.png', 0)
# Lakukan histogram equalization pada gambar dengan kontras rendah
equalized_low_contrast = cv2.equalizeHist(img_low_contrast)
# Hitung histogram gambar asli dan hasil histogram equalization pada gambar dengan kontras rendah
histogram_low = cv2.calcHist([img_low_contrast], [0], None, [256], [0, 256])
equalized_histogram_low = cv2.calcHist([equalized_low_contrast], [0], None, [256], [0, 256])
# Tampilkan gambar asli dan hasil histogram equalization pada gambar dengan kontras rendah
plt.subplot(2, 2, 1)
plt.imshow(img_low_contrast, cmap='gray')
plt.title('Gambar Asli')
plt.subplot(2, 2, 2)
plt.imshow(equalized_low_contrast, cmap='gray')
plt.title('Histogram Equalization')
# Tampilkan histogram gambar asli dan hasil histogram equalization pada gambar dengan kontras rendah
plt.subplot(2, 2, 3)
plt.plot(histogram_low, color='gray')
plt.title('Histogram Gambar Asli')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')
plt.subplot(2, 2, 4)
plt.plot(equalized_histogram_low, color='gray')
plt.title('Histogram Setelah Histogram Equalization')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

# Baca gambar dengan kontras tinggi
img_high_contrast = cv2.imread('tinggi.png', 0)
# Lakukan histogram equalization pada gambar dengan kontras tinggi
equalized_high_contrast = cv2.equalizeHist(img_high_contrast)
# Hitung histogram gambar asli dan hasil histogram equalization pada gambar dengan kontras tinggi
histogram_high = cv2.calcHist([img_high_contrast], [0], None, [256], [0, 256])
equalized_histogram_high = cv2.calcHist([equalized_high_contrast], [0], None, [256], [0, 256])
# Tampilkan gambar asli dan hasil histogram equalization pada gambar dengan kontras tinggi
plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(img_high_contrast, cmap='gray')
plt.title('Gambar Asli')
plt.subplot(2, 2, 2)
plt.imshow(equalized_high_contrast, cmap='gray')
plt.title('Histogram Equalization')
# Tampilkan histogram gambar asli dan hasil histogram equalization pada gambar dengan kontras tinggi
plt.subplot(2, 2, 3)
plt.plot(histogram_high, color='gray')
plt.title('Histogram Gambar Asli')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')
plt.subplot(2, 2, 4)
plt.plot(equalized_histogram_high, color='gray')
plt.title('Histogram Setelah Histogram Equalization')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

# Baca gambar dengan kontras normal
img_normal_contrast = cv2.imread('normal.png', 0)
# Lakukan histogram equalization
equalized_normal_contrast = cv2.equalizeHist(img_normal_contrast)
#Hitung histogram gambar asli dan hasil histogram equalization pada gambar dengan kontras normal
histogram_normal = cv2.calcHist([img_normal_contrast], [0], None, [256], [0, 256])
equalized_histogram_normal = cv2.calcHist([equalized_normal_contrast], [0], None, [256], [0, 256])
#Tampilkan gambar asli dan hasil histogram equalization pada gambar dengan kontras normal
plt.figure()
plt.subplot(2, 2, 1)
plt.imshow(img_normal_contrast, cmap='gray')
plt.title('Gambar Asli')
plt.subplot(2, 2, 2)
plt.imshow(equalized_normal_contrast, cmap='gray')
plt.title('Histogram Equalization')
#Tampilkan histogram gambar asli dan hasil histogram equalization pada gambar dengan kontras normal
plt.subplot(2, 2, 3)
plt.plot(histogram_normal, color='gray')
plt.title('Histogram Gambar Asli')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')
plt.subplot(2, 2, 4)
plt.plot(equalized_histogram_normal, color='gray')
plt.title('Histogram Setelah Histogram Equalization')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

#Tampilkan semua gambar dan histogram
plt.show()