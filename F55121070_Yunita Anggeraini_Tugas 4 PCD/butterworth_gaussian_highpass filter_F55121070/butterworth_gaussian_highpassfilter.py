#Yunita Anggeraini
#F55121070
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load gambar
img = cv2.imread('lena.jpg', 0)

# Transformasi Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Filter Butterworth Highpass
rows, cols = img.shape
crow, ccol = rows//2, cols//2
D0 = 30
n = 4
Butterworth_HP = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
        D = np.sqrt((i-crow)**2 + (j-ccol)**2)
        Butterworth_HP[i, j] = 1 / (1 + (D/D0)**(2*n))

Butterworth_HP_shift = np.fft.fftshift(Butterworth_HP)
filtered_Butterworth_HP = fshift * Butterworth_HP_shift
img_Butterworth_HP = np.fft.ifft2(filtered_Butterworth_HP)
img_Butterworth_HP = np.abs(img_Butterworth_HP)

# Filter Gaussian Highpass
D = 30
Gaussian_HP = np.zeros((rows, cols))
for i in range(rows):
    for j in range(cols):
        Gaussian_HP[i, j] = 1 - np.exp(-((i-crow)**2+(j-ccol)**2)/(2*D**2))

Gaussian_HP_shift = np.fft.fftshift(Gaussian_HP)
filtered_Gaussian_HP = fshift * Gaussian_HP_shift
img_Gaussian_HP = np.fft.ifft2(filtered_Gaussian_HP)
img_Gaussian_HP = np.abs(img_Gaussian_HP)

# Tampilkan gambar hasil filter
plt.subplot(131), plt.imshow(img, cmap='gray')
plt.title('Input Gambar'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(img_Butterworth_HP, cmap='gray')
plt.title('Butterworth Highpass Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(img_Gaussian_HP, cmap='gray')
plt.title('Gaussian Highpass Filter'), plt.xticks([]), plt.yticks([])
plt.show()
