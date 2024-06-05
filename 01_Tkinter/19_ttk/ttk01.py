import tkinter as tk
from tkinter import ttk

def on_combobox_select(event):
    label.config(text=f"Selected: {combo.get()}")

root = tk.Tk()
root.title("ttk.Combobox Example")
root.geometry("300x200")

label = ttk.Label(root, text="Select an option:")
label.pack(pady=10)

combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo.pack(pady=10)
combo.bind("<<ComboboxSelected>>", on_combobox_select)

root.mainloop()