import cv2
import matplotlib.pyplot as plt

# Baca gambar dengan kontras rendah
img_low_contrast = cv2.imread('rendah.png', 0)

# Hitung histogram gambar dengan kontras rendah
histogram_low = cv2.calcHist([img_low_contrast], [0], None, [256], [0, 256])

# Tampilkan histogram gambar dengan kontras rendah
plt.subplot(1, 3, 1)
plt.plot(histogram_low, color='gray')
plt.title('Histogram Kontras Rendah')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

# Baca gambar dengan kontras tinggi
img_high_contrast = cv2.imread('tinggi.png', 0)

# Hitung histogram gambar dengan kontras tinggi
histogram_high = cv2.calcHist([img_high_contrast], [0], None, [256], [0, 256])

# Tampilkan histogram gambar dengan kontras tinggi
plt.subplot(1, 3, 2)
plt.plot(histogram_high, color='gray')
plt.title('Histogram Kontras Tinggi')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

# Baca gambar dengan kontras normal
img_normal_contrast = cv2.imread('normal.png', 0)

# Hitung histogram gambar dengan kontras normal
histogram_normal = cv2.calcHist([img_normal_contrast], [0], None, [256], [0, 256])

# Tampilkan histogram gambar dengan kontras normal
plt.subplot(1, 3, 3)
plt.plot(histogram_normal, color='gray')
plt.title('Histogram Kontras Normal')
plt.xlabel('Intensitas Piksel')
plt.ylabel('Jumlah Piksel')

# Tampilkan grafik histogram
plt.show()