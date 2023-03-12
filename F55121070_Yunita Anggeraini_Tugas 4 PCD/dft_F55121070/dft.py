#Yunita Anggeraini
#F55121070
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load gambar asli
img = cv2.imread('tes1.jpg', cv2.IMREAD_GRAYSCALE)

# Lakukan transformasi DFT
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

# Hitung magnitude spectrum
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# Tampilkan gambar asli dan magnitude spectrum
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Gambar Asli'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# Lakukan inverse transformasi DFT
idft_shift = np.fft.ifftshift(dft_shift)
img_back = cv2.idft(idft_shift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

# Tampilkan hasil inverse transformasi DFT
plt.imshow(img_back, cmap='gray')
plt.title('Hasil Inverse Transformasi DFT'), plt.xticks([]), plt.yticks([])
plt.show()
