# showvalue
import tkinter as tk


def on_scale(val):
    label.config(text=str(val) + "%")

# ウィンドウの作成
root = tk.Tk()
root.title("Scale-完全独学Python")
root.geometry("500x300")

# スライダーの作成
scale = tk.Scale(root, from_=0, to=100, command=on_scale)
scale.pack()

# ラベルの作成
label = tk.Label(root, text="0")
label.pack()

# ウィンドウの表示
root.mainloop()