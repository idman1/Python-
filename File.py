# import pathlib
#
# path = pathlib.Path.cwd()
# folder_a = path / "folder_a"
# print(folder_a)
from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Clock')


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibre', 40, 'underline'),
            background='purple',
            foreground='white')
lbl.pack(anchor='ne')
time()
mainloop()
