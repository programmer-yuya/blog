import tkinter as tk

root = tk.Tk()
root.title("Tkinter Standard Widgets")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=10)

button = tk.Button(root, text="Click Me")
button.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

root.mainloop()
