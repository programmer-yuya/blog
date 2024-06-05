import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Combobox-完全独学Python")
root.geometry("300x200")

# Comboboxの作成
options = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(root, values=options)
combobox.pack(padx=10, pady=10)

# メインループの実行
root.mainloop()
