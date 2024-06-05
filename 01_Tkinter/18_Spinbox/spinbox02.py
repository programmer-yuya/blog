import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Spinbox-完全独学Python")
root.geometry("500x300")

# Spinboxの作成
spinbox = tk.Spinbox(root, values=[10, 20, 30, 40, 50])
spinbox.pack(pady=20)

# メインループの開始
root.mainloop()
