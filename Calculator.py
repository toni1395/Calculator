from tkinter import *

root = Tk()
display = Entry(root, width = 27, borderwidth=5)
display.grid(column=0, row=0, columnspan=3)


def hapus():
    display.delete(0, END)
    
def tambahAngka(angka):
    angkaper = display.get()
    display.delete(0, END)
    display.insert(0, str(angkaper) + str(angka))

def Tambah ():
    angka_pertama = display.get()
    display.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = int(angka_pertama)
    math="tambah"

def Kurang ():
    angka_pertama = display.get()
    display.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = int(angka_pertama)
    math="kurang"

def Bagi ():
    angka_pertama = display.get()
    display.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = int(angka_pertama)
    math="bagi"

def Kali ():
    angka_pertama = display.get()
    display.delete(0, END)
    global angkaFirst
    global math
    angkaFirst = int(angka_pertama)
    math="kali"

def samaDengan():
    angka_kedua = display.get()
    display.delete(0, END)

    if math == "tambah":
        display.insert(0,angkaFirst + int(angka_kedua))
    if math == "kurang":
        display.insert(0,angkaFirst - int(angka_kedua))
    if math == "kali":
        display.insert(0,angkaFirst * int(angka_kedua))
    if math == "bagi":
        display.insert(0,angkaFirst / int(angka_kedua))

angka1=Button(root, text=1, padx=40, pady=40, command=lambda: tambahAngka(1))
angka2=Button(root, text=2, padx=40, pady=40, command=lambda: tambahAngka(2))
angka3=Button(root, text=3, padx=40, pady=40, command=lambda: tambahAngka(3))
angka4=Button(root, text=4, padx=40, pady=40, command=lambda: tambahAngka(4))
angka5=Button(root, text=5, padx=40, pady=40, command=lambda: tambahAngka(5))
angka6=Button(root, text=6, padx=40, pady=40, command=lambda: tambahAngka(6))
angka7=Button(root, text=7, padx=40, pady=40, command=lambda: tambahAngka(7))
angka8=Button(root, text=8, padx=40, pady=40, command=lambda: tambahAngka(8))
angka9=Button(root, text=9, padx=40, pady=40, command=lambda: tambahAngka(9))
angka0=Button(root, text=0, padx=40, pady=40, command=lambda: tambahAngka(0))

hapus = Button(root, text="Hapus", padx=73, pady=40, command=hapus)
samaDengan = Button(root, text="=", padx=87, pady=20,command=samaDengan)
Tambah = Button(root, text="+", padx=40, pady=20,command=Tambah)
Kurang = Button(root, text="-", padx=40, pady=20,command=Kurang)
Bagi = Button(root, text="/", padx=40, pady=20,command=Bagi)
Kali = Button(root, text="*", padx=40, pady=20,command=Kali)


angka1.grid(column=0,row=1)
angka2.grid(column=1,row=1)
angka3.grid(column=2,row=1)

angka4.grid(column=0,row=2)
angka5.grid(column=1,row=2)
angka6.grid(column=2,row=2)

angka7.grid(column=0,row=3)
angka8.grid(column=1,row=3)
angka9.grid(column=2,row=3)

angka0.grid(column=0,row=4)

hapus.grid(column=1, row=4, columnspan=2)
samaDengan.grid(column=1, row=5, columnspan=2)

Tambah.grid(column=0, row=5)
Kurang.grid(column=0, row=6)
Kali.grid(column=1, row=6)

Bagi.grid(column=2, row=6)

root.mainloop()