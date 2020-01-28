import tkinter as tk

import time

class AplCip(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self,default='clienticon.ico')
        tk.Tk.wm_title(self, "Aplikasi Cipher")
        tk.Tk.wm_geometry(self,["1600x8000"])
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        self.localtime = time.asctime(time.localtime(time.time()))

        self.lblInfo = tk.Label(self, font=('Goudy Stout', 40, 'bold'),
                text="\nSELAMAT DATANG \n di \n ENCRYPT & DECRYPT \n APPLICATION",
                fg="black",bd="10", anchor='w')

        self.lblInfo.grid(row=0, column=1)

        self.lblInfo = tk.Label(self, font=('times new roman', 20, 'bold'),
                text=self.localtime, fg="Blue",
                bd=10, anchor='w')

        self.lblInfo.grid(row=1, column=1)

        self.lblInfo = tk.Label(self, font=('times new roman', 16, 'bold'),
                text="Pilih Algoritma!", fg="Blue",
                bd=10, anchor='w')

        self.lblInfo.grid(row=2, column=1)

        self.btn1 = tk.Button(self, padx=8, pady=8, bd=10,
                  fg="black", font=('comic sans ms', 20, 'bold'),
                width=16, text="Algoritma Vigenere", bg="pink",
                  command=lambda: controller.show_frame(PageOne)).grid(row=3, column=1)

        self.btn2 = tk.Button(self, padx=8, pady=8, bd=10,
                  fg="black", font=('comic sans ms', 20, 'bold'),
                  width=16, text="Algoritma Caesar", bg="green",
                  command=lambda: controller.show_frame(PageTwo)).grid(row=4, column=1)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.localtime = time.asctime(time.localtime(time.time()))

        self.lblInfo = tk.Label(self, font=('Goudy Stout', 20, 'bold'),
                text="SECRET MESSAGING \n Vigenère Cipher",
                fg="Dark Red", bd=10, anchor='w')

        self.lblInfo.grid(row=0, column=0)

        self.lblInfo = tk.Label(self, font=('times new roman', 10, 'bold'),
                text=self.localtime, fg="Blue",
                bd=10, anchor='w')

        self.lblInfo.grid(row=1, column=0)

        self.name = tk.StringVar()
        self.Msg = tk.StringVar()
        self.key = tk.StringVar()
        self.mode = tk.StringVar()
        self.Result = tk.StringVar()
        # reference
        # Function to encode
        self.lblReference = tk.Label(self, font=('comic sans ms', 16, 'bold'),
                     text="NAMA:", bd=16, anchor="w")

        self.lblReference.grid(row=2, column=0)

        self.txtReference = tk.Entry(self, font=('comic sans ms', 14, 'bold'),
                     textvariable=self.name, bd=10, insertwidth=4,
                     bg="light blue", justify='right')

        self.txtReference.grid(row=2, column=1)

        # labels
        self.lblMsg = tk.Label(self, font=('comic sans ms', 16, 'bold'),
               text="PESAN:", bd=16, anchor="w")

        self.lblMsg.grid(row=3, column=0)

        self.txtMsg = tk.Entry(self, font=('comic sans ms', 14, 'bold'),
               textvariable=self.Msg, bd=10, insertwidth=4,
               bg="light blue", justify='right')

        self.txtMsg.grid(row=3, column=1)

        self.lblkey = tk.Label(self, font=('comic sans ms', 16, 'bold'),
               text="KUNCI:", bd=16, anchor="w")

        self.lblkey.grid(row=4, column=0)

        self.txtkey = tk.Entry(self, font=('comic sans ms', 14, 'bold'),
               textvariable=self.key, bd=10, insertwidth=4,
               bg="light blue", justify='right')

        self.txtkey.grid(row=4, column=1)

        self.lblmode = tk.Label(self, font=('comic sans ms', 16, 'bold'),
                text="MODE(e untuk enkripsi, d untuk dekripsi):",
                bd=16, anchor="w")

        self.lblmode.grid(row=5, column=0)

        self.txtmode = tk.Entry(self, font=('comic sans ms', 14, 'bold'),
                textvariable=self.mode, bd=10, insertwidth=4,
                bg="light blue", justify='right')

        self.txtmode.grid(row=5, column=1)

        self.lblService = tk.Label(self, font=('comic sans ms', 16, 'bold'),
                   text="Hasil Enkripsi/Dekripsi:", bd=16, anchor="w")

        self.lblService.grid(row=4, column=2)

        self.txtService = tk.Entry(self, font=('arial', 14, 'bold'),
                   textvariable=self.Result, bd=10, insertwidth=4,
                   bg="light blue", justify='right')

        self.txtService.grid(row=4, column=3)

        self.btnBack = tk.Button(self, padx=16, pady=8, bd=16, fg="black",
                  font=('comic sans ms', 16, 'bold'), width=10,
                  text="Kembali", bg="pink",
                  command=lambda: controller.show_frame(StartPage)).grid(row=9, column=0)

        # Show message button
        self.btnTotal = tk.Button(self, padx=16, pady=8, bd=16, fg="black",
                  font=('comic sans ms', 16, 'bold'), width=10,
                  text="Lihat Hasilnya!", bg="pink",
                  command=self.Alg).grid(row=9, column=1)

        # Reset button
        self.btnReset = tk.Button(self, padx=16, pady=8, bd=16,
                  fg="black", font=('comic sans ms', 16, 'bold'),
                  width=10, text="Coba lagi!", bg="green",
                  command=self.Reset).grid(row=9, column=2)

        # Exit button
        self.btnExit = tk.Button(self, padx=16, pady=8, bd=16,
                 fg="black", font=('comic sans ms', 16, 'bold'),
                 width=10, text="Selesai!", bg="yellow",
                 command=self.qExit).grid(row=9, column=3)

    def Alg(self):
        print("Pesan= ", (self.Msg.get()))

        self.clear = self.Msg.get()
        self.k = self.key.get()
        self.m = self.mode.get()
        if (self.m == 'e'):
            self.Result.set(self.encode(self.k, self.clear))
        else:
            self.Result.set(self.decode(self.k, self.clear))

    def Reset(self):
        self.name.set("")
        self.Msg.set("")
        self.key.set("")
        self.mode.set("")
        self.Result.set("")
    def qExit(self):
            tk._exit()
    # Function to encode
    def encode(self,key, clear):
        clear = clear.upper()
        key = key.upper()
        cipher = ""
        i, j = 0, 0
        while i < len(clear):
            if clear[i].isalpha():
                huruf = chr((((ord(clear[i]) - 65) + (ord(key[j]) - 65)) % 26) + 65)
                j = (j + 1) % len(key)
            else:
                huruf = clear[i]
            i = i + 1
            cipher = cipher + huruf
            print(cipher)
        return cipher
    def decode(self,key, cipher):
        cipher = cipher.upper()
        key = key.upper()
        plain = ""
        i, j = 0, 0
        while i < len(cipher):
            if cipher[i].isalpha():
                huruf = chr((((ord(cipher[i]) - 65) - (ord(key[j]) - 65)) % 26) + 65)
                j = (j + 1) % len(key)
            else:
                huruf = cipher[i]
            i = i + 1
            plain = plain + huruf
            print(plain)
        return plain



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.localtime = time.asctime(time.localtime(time.time()))

        self.lblInfo = tk.Label(self, font=('Goudy Stout', 20, 'bold'),
                text="SECRET MESSAGING \n Caesar Cipher",
                fg="Dark Red", bd=10, anchor='w')

        self.lblInfo.grid(row=0, column=0)

        self.lblInfo = tk.Label(self, font=('times new roman', 10, 'bold'),
                text=self.localtime, fg="Blue",
                bd=10, anchor='w')

        self.lblInfo.grid(row=1, column=0)

        self.name = tk.StringVar()
        self.Msg = tk.StringVar()
        self.key = tk.StringVar()
        self.mode = tk.StringVar()
        self.Result = tk.StringVar()


        # reference
        self.lblReference = tk.Label(self, font=('comic sans ms', 16, 'bold'),
                     text="NAMA:", bd=16, anchor="w")

        self.lblReference.grid(row=2, column=0)

        self.txtReference = tk.Entry(self, font=('comic sans ms', 14, 'bold'),
                     textvariable=self.name, bd=10, insertwidth=4,
                     bg="light blue", justify='right')

        self.txtReference.grid(row=2, column=1)

        # labels
        self.lblMsg = tk.Label(self, font=('comic sans ms', 16, 'bold'),
               text="PESAN:", bd=16, anchor="w")

        self.lblMsg.grid(row=3, column=0)

        self.txtMsg = tk.Entry(self, font=('comic sans ms', 14, 'bold'),
               textvariable=self.Msg, bd=10, insertwidth=4,
               bg="light blue", justify='right')

        self.txtMsg.grid(row=3, column=1)

        self.lblkey = tk.Label(self, font=('comic sans ms', 16, 'bold'),
               text="KUNCI(harus angka):", bd=16, anchor="w")

        self.lblkey.grid(row=4, column=0)

        self.txtkey = tk.Entry(self, font=('comic sans ms', 14, 'bold'),
               textvariable=self.key, bd=10, insertwidth=4,
               bg="light blue", justify='right')

        self.txtkey.grid(row=4, column=1)

        self.lblmode = tk.Label(self, font=('comic sans ms', 16, 'bold'),
                text="MODE(e untuk enkripsi, d untuk dekripsi):",
                bd=16, anchor="w")

        self.lblmode.grid(row=5, column=0)

        self.txtmode = tk.Entry(self, font=('comic sans ms', 14, 'bold'),
                textvariable=self.mode, bd=10, insertwidth=4,
                bg="light blue", justify='right')

        self.txtmode.grid(row=5, column=1)

        self.lblService = tk.Label(self, font=('comic sans ms', 16, 'bold'),
                   text="Hasil Enkripsi/Dekripsi:", bd=16, anchor="w")

        self.lblService.grid(row=5, column=2)

        self.txtService = tk.Entry(self, font=('arial', 14, 'bold'),
                   textvariable=self.Result, bd=10, insertwidth=4,
                   bg="light blue", justify='right')

        self.txtService.grid(row=5, column=3)

        self.btnBack = tk.Button(self, padx=16, pady=8, bd=16, fg="black",
                  font=('comic sans ms', 16, 'bold'), width=10,
                  text="Kembali", bg="pink",
                  command=lambda: controller.show_frame(StartPage)).grid(row=7, column=0)

        self.btnTotal = tk.Button(self, padx=16, pady=8, bd=16, fg="black",
                  font=('comic sans ms', 16, 'bold'), width=10,
                  text="Lihat Hasilnya!", bg="pink",
                  command=self.Alg).grid(row=7, column=1)

        # Reset button
        self.btnReset = tk.Button(self, padx=16, pady=8, bd=16,
                  fg="black", font=('comic sans ms', 16, 'bold'),
                  width=10, text="Coba lagi!", bg="green",
                  command=self.Reset).grid(row=7, column=2)

        # Exit button
        self.btnExit = tk.Button(self, padx=16, pady=8, bd=16,
                 fg="black", font=('comic sans ms', 16, 'bold'),
                 width=10, text="Selesai!", bg="yellow",
                 command=self.qExit).grid(row=7, column=3)        


        # Caesar cipher
        # Function to encode
    def encode(self,key, clear):
        clear = clear.upper()
        cipher = ""
        i = 0
        while i < len(clear):
            if clear[i].isalpha():
                huruf = chr((((ord(clear[i]) - 65) + key) % 26) + 65)
            else:
                huruf = clear[i]
            i = i + 1
            cipher = cipher + huruf
            print(cipher)
        return cipher
    # Function to decode
    def decode(self,key, cipher):
        cipher = cipher.upper()
        plain = ""
        i = 0
        while i < len(cipher):
            if cipher[i].isalpha():
                huruf = chr((((ord(cipher[i]) - 65) - key) % 26) + 65)                
            else:
                huruf = cipher[i]
            i = i + 1
            plain = plain + huruf
            print(plain)
        return plain
    def Alg(self):
        print("Pesan= ", (self.Msg.get()))
        self.clear = self.Msg.get()
        self.k = int(self.key.get())
        self.m = self.mode.get()
        if (self.m == 'e'):
            self.Result.set(self.encode(self.k, self.clear))
        else:
            self.Result.set(self.decode(self.k, self.clear))
        # Show message button
    # exit function
    def qExit(self):
        tk._exit()
    #tombol Reset
    def Reset(self):
        self.name.set("")
        self.Msg.set("")
        self.key.set("")
        self.mode.set("")
        self.Result.set("")
        


app = AplCip()
app.mainloop()
