#GUI = graphical User Interface
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


#membuat window
window = tk.Tk() #gawe window ne
window.configure(bg="gray") #begron
window.geometry("300x200")#ukuran window
window.title("halo") #judul
window.resizable(False,False)#iki (x,y) ben gak iso di ubah ubah

#variable
NAMA_BELAKANG =tk.StringVar() #jenis data
NAMA_DEPAN =tk.StringVar()#jenis data

 #frame input 
input_frame =ttk.Frame(window)
#penempatan grid,pack place
input_frame.pack(padx=10,pady=30,fill="x",expand=True)

#komponen-komponen
#1.Label untuk nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan : ")
nama_depan_label.pack(padx=10,fill="x",expand=True)
#2.entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
#3.label untuk nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang : ")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
#4.entry nama depan
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
#5.tombol
def tombol_click():
    '''fungsi ini akan di panggil oleh tombol'''
    pesan = f"Halo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} ,BRUUUUUHHHHH"
    showinfo(title="hehe",message=pesan)

tombol_sapa = ttk.Button(input_frame,text="sapa",command=tombol_click)
tombol_sapa.pack(fill="x",expand=True,padx=1,pady=10)

window.mainloop() # iki kyok loop tanpa henti

