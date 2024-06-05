import tkinter as tk
from tkinter import ttk

def on_combobox_selected(event):
    selected_value = combobox.get()
    label.config(text=f"Selected: {selected_value}")

root = tk.Tk()
root.title("Combobox-選択変更イベント")
root.geometry("300x200")

# Comboboxの作成
options = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(root, values=options)
combobox.pack(padx=10, pady=10)

# ラベルの作成
label = ttk.Label(root, text="Selected: ")
label.pack(padx=10, pady=10)

# Comboboxの選択変更イベントをバインド
combobox.bind("<<ComboboxSelected>>", on_combobox_selected)

root.mainloop()
