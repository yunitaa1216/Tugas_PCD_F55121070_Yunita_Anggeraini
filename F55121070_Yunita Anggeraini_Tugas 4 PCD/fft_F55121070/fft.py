#Yunita Anggeraini
#F55121070
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load gambar asli
img = cv2.imread('batik.jpeg', cv2.IMREAD_GRAYSCALE)

# Lakukan transformasi Fourier
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

# Hitung magnitude spectrum
magnitude_spectrum = 20 * np.log(np.abs(fshift))

# Tampilkan gambar asli dan magnitude spectrum
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# Lakukan inverse transformasi Fourier
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

# Tampilkan hasil inverse transformasi Fourier
plt.imshow(img_back, cmap='gray')
plt.title('Hasil Inverse Transformasi Fourier'), plt.xticks([]), plt.yticks([])
plt.show()