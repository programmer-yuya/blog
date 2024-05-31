import tkinter as tk

root = tk.Tk()
root.title("Grid-完全独学Python")
root.geometry("500x300")

label1 = tk.Label(root, text="Label 1", bg="lightblue")
label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label3 = tk.Label(root, text="Label 3", bg="lightcoral")
label4 = tk.Label(root, text="Label 4", bg="lightyellow")

label1.grid(row=0, column=0, rowspan=2)
label2.grid(row=0, column=1, columnspan=2)
label3.grid(row=1, column=1)
label4.grid(row=1, column=2)

root.mainloop()
