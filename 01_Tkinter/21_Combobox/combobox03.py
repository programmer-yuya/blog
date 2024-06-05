import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox- widthオプション")
root.geometry("300x200")

# Comboboxの作成（幅5文字分）
options = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(root, values=options, width=5)
combobox.pack(padx=10, pady=10)

root.mainloop()
