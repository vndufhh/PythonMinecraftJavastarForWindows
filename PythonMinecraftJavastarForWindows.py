#導入Tkinter
from tkinter import*
#基本設定
win = Tk()
win.title("main")
win.geometry("999x600")
win.resizable(False,False)
menubar = Menu(win)              # 建立主選單
menubar.add_command(label="Exit")    # 主選單項目
win.config(menu=menubar)             # 主視窗加入主選單
win.mainloop()