#Yunita Anggeraini
#F55121070
import cv2

# membaca gambar
img = cv2.imread('lena.jpg')

# konversi gambar menjadi grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# melakukan median filter dengan kernel 3x3
median_3x3 = cv2.medianBlur(gray, 3)

# melakukan median filter dengan kernel 5x5
median_5x5 = cv2.medianBlur(gray, 5)

# menampilkan gambar asli dan hasil median filter
cv2.imshow('Original Image', gray)
cv2.imshow('Median Filter 3x3', median_3x3)
cv2.imshow('Median Filter 5x5', median_5x5)

# menunggu tombol keyboard ditekan
cv2.waitKey(0)

# menutup semua jendela
cv2.destroyAllWindows()