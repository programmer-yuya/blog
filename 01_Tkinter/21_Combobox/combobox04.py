import tkinter as tk
from tkinter import ttk

def update_options():
    new_options = ["Updated 1", "Updated 2", "Updated 3"]
    combobox['values'] = new_options

root = tk.Tk()
root.title("Combobox- postcommandオプション")
root.geometry("300x200")

# Comboboxの作成
options = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(root, values=options, postcommand=update_options)
combobox.pack(padx=10, pady=10)

root.mainloop()
