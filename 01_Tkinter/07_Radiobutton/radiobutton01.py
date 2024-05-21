# ラジオボタンの基本
import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Radiobutton-完全独学Python")
root.geometry("500x300")

# ラジオボタンの作成
radiobutton01 = tk.Radiobutton(root, text="ラジオボタン１")
radiobutton01.pack()

radiobutton02 = tk.Radiobutton(root, text="ラジオボタン２")
radiobutton02.pack()

radiobutton03 = tk.Radiobutton(root, text="ラジオボタン３")
radiobutton03.pack()

# ウィンドウの表示
root.mainloop()