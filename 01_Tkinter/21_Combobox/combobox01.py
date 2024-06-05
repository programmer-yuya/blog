import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox- valuesオプション")
root.geometry("300x200")

# Comboboxの作成
options = ("Option A", "Option B", "Option C")
combobox = ttk.Combobox(root, values=options)
combobox.pack(padx=10, pady=10)

root.mainloop()
