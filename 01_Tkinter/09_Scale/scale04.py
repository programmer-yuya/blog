# length
import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Scale-完全独学Python")
root.geometry("500x300")

# スライダーの作成
scale01 = tk.Scale(root, from_=0, to=100, length=50)
scale01.pack()

scale02 = tk.Scale(root, from_=0, to=100, length=300)
scale02.pack()

# ウィンドウの表示
root.mainloop()