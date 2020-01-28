from tkinter import *
from Crypto.Hash import SHA512, SHA224
from PIL import Image
from tkinter import messagebox, Frame, Tk, filedialog
import stepic
from tkinter import ttk

def cek ():
    tipeFile = [('images', '*.jpg , *.png, *.jpeg')]
    buka = filedialog.askopenfilename(initialdir="/home", filetypes=tipeFile)
    gambar.insert(10, buka)
def cekgb ():
    tipeFile = [("images", "*.bmp")]
    buka = filedialog.askopenfilename(initialdir="/home", filetypes=tipeFile)
    filestega.insert(10, buka)
def gaskeun():
    if pesan.get()=='' :
        messagebox.showerror("Perhatian!!", "Pesan tidak boleh kosong!")
    elif gambar.get()=='' :
        messagebox.showerror("Perhatian!!", "Gambar tidak boleh kosong!!")
    else :
        f = Image.open(gambar.get())
        a = bytes(pesan.get(), 'utf-8')
        steg = stepic.encode(f, a)
        tipeFile = [('image.bmp', '*.bmp')]
        g = filedialog.asksaveasfilename(title="simpan steganografi", initialdir="/home", filetypes=tipeFile)
        dirgb.insert(10, g)
        inigb = dirgb.get()
        steg.save(inigb)
        messagebox.showinfo("Perhatian!!","Steganografi berhasil!!")
def gaskuy():
    if pesan.get()=='' :
        messagebox.showerror("Perhatian!!", "Pesan tidak boleh kosong!")
    elif gambar.get()=='' :
        messagebox.showerror("Perhatian!!", "Gambar tidak boleh kosong!!")
    else :
        f = Image.open(gambar.get())
        a = bytes(pesan.get(), 'utf-8')
        steg = stepic.encode(f, a)
        tipeFile = [('image', '*.bmp')]
        g = filedialog.asksaveasfilename(title="simpan steganografi", initialdir="/home", filetypes=tipeFile)
        dirgb.insert(10, g)
        inigb = dirgb.get()
        steg.save(inigb)
        BLOCKSIZE = 65536
        hasher = SHA512.new()
        with open(inigb, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        h = hasher.hexdigest()
        #sh = filedialog.asksaveasfilename(title="simpan hash(SHA-3)", initialdir="/home", filetypes=[("text", "*.txt")])
        #foo = open(sh, "w")
        #foo.write(h)
        dirsh.insert(10, h)
        #foo.close
        messagebox.showinfo("Perhatian!!", "Steganografi dan hash berhasil!!")
def gaskuy2():
    if pesan.get() == '':
        messagebox.showerror("Perhatian!!", "Pesan tidak boleh kosong!")
    elif gambar.get() == '':
        messagebox.showerror("Perhatian!!", "Gambar tidak boleh kosong!!")
    else:
        f = Image.open(gambar.get())
        a = bytes(pesan.get(), 'utf-8')
        steg = stepic.encode(f, a)
        tipeFile = [('image', '*.bmp')]
        g = filedialog.asksaveasfilename(title="simpan steganografi", initialdir="/home", filetypes=tipeFile)
        dirgb.insert(10, g)
        inigb = dirgb.get()
        steg.save(inigb)
        BLOCKSIZE = 65536
        hasher = SHA224.new()
        with open(inigb, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        h1 = hasher.hexdigest()
        #sh = filedialog.asksaveasfilename(title="simpan hash(SHA-2)", initialdir="/home", filetypes=[("text", "*.txt")])
        #foo = open(sh, "w")
        #foo.write(h1)
        dirsh2.insert(50, h1)
        #foo.close
        messagebox.showinfo("Perhatian!!", "Steganografi dan hash berhasil!!")
def gaskuy3():
    f = Image.open(gambar.get())
    if pesan.get() == '':
        messagebox.showerror("Perhatian!!", "Pesan tidak boleh kosong!")
    else:
        a = bytes(pesan.get(), 'utf-8')
        steg = stepic.encode(f, a)
        tipeFile = [('image', '*.bmp')]
        g = filedialog.asksaveasfilename(title="simpan steganografi", initialdir="/home", filetypes=tipeFile)
        dirgb.insert(10, g)
        inigb = dirgb.get()
        steg.save(inigb)
        BLOCKSIZE = 65536
        hasher = SHA512.new()
        with open(inigb, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        h = hasher.hexdigest()
        #sh = filedialog.asksaveasfilename(title="simpan hash(SHA-3 + SHA-2)", initialdir="/home", filetypes=[("text", "*.txt")])
        #foo = open(sh, "w")
        #foo.write(h)
        dirsh.insert(50, h)
        #foo.close

        BLOCKSIZE = 65536
        hasher = SHA224.new()
        with open(inigb, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        h1 = hasher.hexdigest()
        #foo = open("stegash_hash.txt", "w+")
        #foo.write(h1)
        dirsh2.insert(50, h1)
        #foo.close

        messagebox.showinfo("Perhatian!!", "Steganografi dan hash berhasil!!")
def bantuan():
    messagebox.showinfo("About Us", "Selamat datang di STEGHASH\n\nDeveloped By:\n- M. Subkhan A\n- Berry Karo-Karo\n- Catur Adi Nugroho\n- M. Aldi Rachman\n- Tanto Nur Atmojo\n\nPertanyaan:\nHubungi : IIIrks.red.@stsn-nci.ac.id \n\n\n©copyright IIIRKSRED19/20 KELOMPOK 3")
def lagi():
    gambar.delete(0, END)
    pesan.delete(0, END)
    dirsh.delete(0, END)
    dirsh2.delete(0, END)
    dirgb.delete(0, END)
    filestega.delete(0, END)
    sha3.delete(0, END)
    sha2.delete(0,END)

def pilih():
    if CheckVar1.get()== 2:
        if CheckVar2.get() == 2 :
            B = Button(TAB1, text="LET'S DO THIS", command=gaskeun)
            B.place(x=170,y=275)
        elif CheckVar2.get() == 1 :
            B = Button(TAB1, text="LET'S DO THIS", command=gaskuy2)
            B.place(x=170, y=275)
    elif CheckVar1.get()==1 :
        if CheckVar2.get() == 2 :
            B = Button(TAB1, text="LET'S DO THIS", command=gaskuy)
            B.place(x=170,y=275)
        elif CheckVar2.get() == 1 :
            B = Button(TAB1, text="LET'S DO THIS", command=gaskuy3)
            B.place(x=170, y=275)
def tutup():
    top.destroy()

def tengok():
    if cekhash1.get() == 2:
        if cekhash2.get() == 2:
            B = Button(TAB2, text="LET'S DO THIS", command=gasaja)
            B.place(x=145, y=220)
        elif cekhash2.get() == 1:
            B = Button(TAB2, text="LET'S DO THIS", command=gasbro2)
            B.place(x=145, y=220)
    elif cekhash1.get() == 1:
        if cekhash2.get() == 2:
            B = Button(TAB2, text="LET'S DO THIS", command=gasbro)
            B.place(x=145, y=220)
        elif cekhash2.get() == 1:
            B = Button(TAB2, text="LET'S DO THIS", command=gasbro3)
            B.place(x=145, y=220)

def gasaja() :
    if  filestega.get() == '' :
        messagebox.showerror("Perhatian!!", "Masukkan gambar terlebih dahulu!!")
    else :
        k = Image.open(filestega.get())
        steg = stepic.decode(k)
        hasilpesan.insert(10, steg)
        d = filedialog.asksaveasfilename(title="simpan pesan", initialdir="/home", filetypes=[("text", "*.txt")])
        iki = open(d, "w")
        iki.write(steg)
        iki.close
        messagebox.showinfo("Sukses!", "Decode berhasil!!")
def gasbro() :
    if  filestega.get() == '' :
        messagebox.showerror("Perhatian!!", "Masukkan gambar terlebih dahulu!!")
    else :
        k = Image.open(filestega.get())
        steg = stepic.decode(k)
        hasilpesan.insert(10, steg)
        d = filedialog.asksaveasfilename(title="simpan pesan", initialdir="/home", filetypes=[("text", "*.txt")])
        iki = open(d, "w")
        iki.write(steg)
        iki.close
        BLOCKSIZE = 65536
        hasher = SHA512.new()
        with open(filestega.get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        h = hasher.hexdigest()
        if h == sha3.get() :
            messagebox.showinfo("Validasi", "SHA-3 valid")
        else:
            messagebox.showerror("Validasi", "SHA-3 tidak valid")
def gasbro2():
    if  filestega.get() == '' :
        messagebox.showerror("Perhatian!!", "Masukkan gambar terlebih dahulu!!")
    else :
        k = Image.open(filestega.get())
        steg = stepic.decode(k)
        hasilpesan.insert(10, steg)
        d = filedialog.asksaveasfilename(title="simpan pesan", initialdir="/home", filetypes=[("text", "*.txt")])
        iki = open(d, "w")
        iki.write(steg)
        iki.close
        BLOCKSIZE = 65536
        hasher = SHA224.new()
        with open(filestega.get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        h = hasher.hexdigest()
        if h == sha2.get() :
            messagebox.showinfo("Validasi", "SHA-2 valid")
        else:
            messagebox.showerror("Validasi", "SHA-2 tidak valid")
def gasbro3():
    if  filestega.get() == '' :
        messagebox.showerror("Perhatian!!", "Masukkan gambar terlebih dahulu!!")
    else :
        k = Image.open(filestega.get())
        steg = stepic.decode(k)
        hasilpesan.insert(10, steg)
        d = filedialog.asksaveasfilename(title="simpan pesan", initialdir="/home", filetypes=[("text", " *.txt")])
        iki = open(d, "w")
        iki.write(steg)
        iki.close
        BLOCKSIZE = 65536
        hasher = SHA512.new()
        with open(filestega.get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        ha3 = hasher.hexdigest()
        BLOCKSIZE = 65536
        hasher = SHA224.new()
        with open(filestega.get(), 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        h = hasher.hexdigest()
        if ha3 == sha3.get():
            if h == sha2.get():
                messagebox.showinfo("Validasi", "SHA-3 dan SHA-2 valid")
            elif h != sha2.get():
                messagebox.showerror("Validasi", "SHA-2 tidak valid")
            else:
                messagebox.showerror("Validasi", "SHA-3 tidak valid")



top = Tk()
top.geometry("800x600")

#Create Tab Control
TAB_CONTROL = ttk.Notebook(top)
#Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='ENCODE')
#Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='DECODE')


#myframe.master.title("STEGHASH")
labelframe = LabelFrame(TAB1, text="STEGANOGRAFI & HASH RKS RED", font=("Calibri",20))
labelframe.pack(pady=10, fill=BOTH, expand="no")
left = Label(labelframe, text="ENCODE YOUR PICTURE", font=("Calibri",50))
left.pack()

labelframe = LabelFrame(TAB2, text="STEGANOGRAFI & HASH RKS RED", font=("Calibri",20))
labelframe.pack(pady=10, fill=BOTH, expand="no")
left = Label(labelframe, text="DECODE YOUR PICTURE", font=("Calibri",50))
left.pack()

komponen1 = Frame(TAB1)

L1 = Label(komponen1, text="MASUKKAN PESAN", width=21)
L1.pack(side=LEFT,anchor=N, padx=5, pady=10)

pesan = Entry(komponen1, bd=2)
pesan.pack(fill=BOTH, pady=5, padx=5)

komponen1.pack(fill=BOTH,pady=5)

komponen2 = Frame(TAB1)

L2 = Label(komponen2, text="MASUKAN GAMBAR", width=20)
L2.pack(side=LEFT, padx=5, pady=10)

gambar = Entry(komponen2, bd=2)
gambar.pack(fill=X, padx=5, pady=5)

tombol = Button(komponen2, text="Browse Gambar", command=cek)
tombol.pack(fill=X, side=LEFT, padx=5,pady=0)

komponen2.pack(fill=X, padx=5,pady=10,anchor=N)

komponen3 = Frame(TAB1)

CheckVar1=IntVar()
C1=Checkbutton(komponen3, text="HASH (SHA-3)", command=pilih, variable=CheckVar1, onvalue=1, offvalue=2 )
C1.pack(side=LEFT)
C1.deselect()

CheckVar2=IntVar()
C2=Checkbutton(komponen3, text="HASH (SHA-2)", command=pilih, variable=CheckVar2, onvalue=1, offvalue=2 )
C2.pack(side=LEFT)
C2.deselect()

komponen3.pack(side=TOP, anchor=N)

komponen4= Frame(TAB1)

ulang = Button(komponen4, text="Retry", command=lagi)
ulang.pack(padx=5,pady=5, side=LEFT)

ex = Button(komponen4, text="Exit", command=tutup)
ex.pack(padx=5, pady=5, side=LEFT)

tolong = Button(komponen4, text="About Us", command=bantuan)
tolong.pack(padx=5, pady=5, side=RIGHT)

komponen4.pack(fill=BOTH, side=BOTTOM, padx= 30, pady=30)

komponen5 = Frame(TAB1)

L5 = Label(komponen5, text="HASIL HASH(SHA-3)", width=21)
L5.pack(side=LEFT,anchor=N, padx=5, pady=5)

dirsh = Entry(komponen5, bd=2)
dirsh.pack(fill=BOTH, pady=5, padx=5)

komponen5.pack(fill=BOTH,pady=20)

komponen6 = Frame(TAB1)

L6 = Label(komponen6, text="HASIL HASH(SHA-2)", width=21)
L6.pack(side=LEFT,anchor=N, padx=5, pady=5)

dirsh2 = Entry(komponen6, bd=2)
dirsh2.pack(fill=BOTH, pady=5, padx=6)

komponen6.pack(fill=BOTH,pady=0)

komponen7 = Frame(TAB1)

L7 = Label(komponen7, text="File saved", width=21)
L7.pack(side=LEFT,anchor=N, padx=5, pady=10)
dirgb = Entry(komponen7, bd=2)
dirgb.pack(fill=BOTH, pady=9, padx=7)
L0 = Label(komponen7, text="(tulis file disertai format .bmp (contoh: example.bmp))" , width=100)
L0.pack(side=LEFT,anchor=N, padx=5, pady=0)

komponen7.pack(fill=BOTH,pady=10)

komponen8 = Frame(TAB2)

L8 = Label(komponen8, text="Masukkan file stega", width=17)
L8.pack(side=LEFT,anchor=N, padx=5, pady=5)

filestega = Entry(komponen8, bd=2)
filestega.pack(fill=BOTH, pady=5, padx=10)

tombol2 = Button(komponen8, text="Browse Stega", command=cekgb)
tombol2.pack(side=LEFT,padx=10,pady=10)

komponen8.pack(fill=X,pady=0)


komponen00 = Frame(TAB2)

cekhash1=IntVar()
C3=Checkbutton(komponen00, text="cek validasi HASH (SHA-3)", command=tengok, variable=cekhash1, onvalue=1, offvalue=2 )
C3.pack(fill=Y, side=LEFT)
C3.deselect()

cekhash2=IntVar()
C4=Checkbutton(komponen00, text="cek validasi HASH (SHA-2)", command=tengok, variable=cekhash2, onvalue=1, offvalue=2 )
C4.pack(fill=Y, side=LEFT)
C4.deselect()

komponen00.pack(side=TOP, anchor=N)

komponen9 = Frame(TAB2)
komponen9.pack(fill=BOTH,pady=0)
L9 = Label(komponen9, text="Hasil Pesan stega", width=17)
L9.pack(side=LEFT,anchor=N, padx=5, pady=5)
hasilpesan = Entry(komponen9, bd=2)

hasilpesan.pack(fill=BOTH, pady=13, padx=9)

komponen10 = Frame(TAB2)

L10 = Label(komponen10, text="Cek validasi SHA-3", width=17)
L10.pack(side=LEFT,anchor=N, padx=5, pady=5)
sha3 = Entry(komponen10, bd=2)
sha3.pack(fill=BOTH, pady=15, padx=10)

komponen10.pack(fill=BOTH,pady=0)

komponen11 = Frame(TAB2)

L11 = Label(komponen11, text="Cek validasi SHA-2", width=17)
L11.pack(side=LEFT,anchor=N, padx=5, pady=5)
sha2 = Entry(komponen11, bd=2)
sha2.pack(fill=BOTH, pady=17, padx=11)

komponen11.pack(fill=BOTH,pady=0)

komponen12= Frame(TAB2)

ulang1 = Button(komponen12, text="Retry", command=lagi)
ulang1.pack(padx=5,pady=5, side=LEFT)

ex1 = Button(komponen12, text="Exit", command=tutup)
ex1.pack(padx=5, pady=5, side=LEFT)

tolong1 = Button(komponen12, text="About Us", command=bantuan)
tolong1.pack(padx=5, pady=5, side=RIGHT)

komponen12.pack(fill=BOTH, side=BOTTOM, padx= 30, pady=30)

TAB_CONTROL.pack(expand=1, fill="both")
top.mainloop()
