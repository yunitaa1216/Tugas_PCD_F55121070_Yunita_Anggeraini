#Yunita Anggeraini F55121070
#Aplikasi perbaikan citra dengan metode penghalusan dan penajaman serta menggunakan library tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2

# Fungsi untuk melakukan perbaikan penghalusan
def smoothing():
    global img
    # Ubah citra menjadi grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Lakukan filter Gaussian untuk menghilangkan noise pada citra
    smoothed = cv2.GaussianBlur(gray, (5, 5), 0)
    # Tampilkan citra yang sudah diubah ke dalam aplikasi
    img_tk = ImageTk.PhotoImage(Image.fromarray(smoothed))
    canvas.create_image(0, 0, anchor=NW, image=img_tk)
    canvas.image = img_tk

# Fungsi untuk melakukan perbaikan penajaman
def sharpening():
    global img
    # Ubah citra menjadi grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Lakukan filter sharpening dengan menggunakan operator Laplacian
    sharpened = cv2.Laplacian(gray, cv2.CV_64F)
    # Tampilkan citra yang sudah diubah ke dalam aplikasi
    img_tk = ImageTk.PhotoImage(Image.fromarray(sharpened))
    canvas.create_image(0, 0, anchor=NW, image=img_tk)
    canvas.image = img_tk

# Fungsi untuk membuka citra
def open_image():
    global img
    # Buka dialog untuk memilih citra
    path = filedialog.askopenfilename()
    # Baca citra
    img = cv2.imread(path)
    # Tampilkan citra ke dalam aplikasi
    img_tk = ImageTk.PhotoImage(Image.fromarray(img))
    canvas.create_image(0, 0, anchor=NW, image=img_tk)
    canvas.image = img_tk

# Membuat jendela utama aplikasi
root = Tk()
root.title("Aplikasi Perbaikan Citra Yunita Anggeraini F55121070")

# Ubah warna latar belakang jendela utama menjadi grey
root.configure(bg='grey')

# Membuat menu bar
menubar = Menu(root)
root.config(menu=menubar)

# Membuat Label untuk menampilkan nama
nama_label = Label(root, text="Yunita Anggeraini F55121070", font=("Helvetica", 10), pady=10, bg='grey')
nama_label.pack()

# Membuat Label untuk menampilkan kelas
kelas_label = Label(root, text="Kelas B", font=("Helvetica", 10), pady=10, bg='grey')
kelas_label.pack()

# Membuat menu "File"
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_image)

# Membuat menu "Penghalusan"
halusmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Penghalusan", command=smoothing)

# Membuat menu "Penajaman"
tajammenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Penajaman", command=sharpening)

# Membuat canvas untuk menampilkan citra
canvas = Canvas(root, width=500, height=500, bg='grey')
canvas.pack()

#Menjalankan aplikasi
root.mainloop()