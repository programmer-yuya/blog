import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("ttk Themed Widgets")
root.geometry("300x200")

label = ttk.Label(root, text="Hello, ttk!")
label.pack(pady=10)

button = ttk.Button(root, text="Click Me")
button.pack(pady=10)

entry = ttk.Entry(root)
entry.pack(pady=10)

root.mainloop()
