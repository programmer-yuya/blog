import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Spinbox-完全独学Python")
root.geometry("500x300")

# Spinboxの作成
def on_spinbox_change():
    result_label.config(text=f"Value changed to: {spinbox.get()}")

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

spinbox = tk.Spinbox(root, from_=0, to=10, command=on_spinbox_change)
spinbox.pack(pady=20)

# メインループの開始
root.mainloop()
