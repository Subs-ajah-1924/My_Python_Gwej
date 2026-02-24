# contoh package/library seng nggowo metode oop/class
import tkinter
 
main_window = tkinter.Tk()

# object
label_1 = tkinter.Label(main_window, text="Label 1")
label_2 = tkinter.Label(main_window, text="Label 2")

button_1 = tkinter.Button(main_window, text="Tombol 1")
button_2 = tkinter.Button(main_window, text="Tombol 2")

# metodh positioning
label_1.pack()
label_2.pack()

button_1.pack()
button_2.pack()

# metodh menampilkan GUI
main_window.mainloop()