#�ɤJTkinter
from tkinter import*
#�򥻳]�w
win = Tk()
win.title("main")
win.geometry("999x600")
win.resizable(False,False)
menubar = Menu(win)              # �إߥD���
menubar.add_command(label="Exit")    # �D��涵��
win.config(menu=menubar)             # �D�����[�J�D���
win.mainloop()