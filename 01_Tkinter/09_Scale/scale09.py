# showvalue
import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Scale-完全独学Python")
root.geometry("500x300")

# スライダーの作成
scale = tk.Scale(root, from_=0, to=100, showvalue=False)
scale.pack()

# ウィンドウの表示
root.mainloop()