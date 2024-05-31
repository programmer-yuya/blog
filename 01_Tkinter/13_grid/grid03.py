import tkinter as tk

root = tk.Tk()
root.title("Grid-完全独学Python")
root.geometry("500x300")

label1 = tk.Label(root, text="Label 1", bg="lightblue")
label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label3 = tk.Label(root, text="Label 3", bg="lightcoral")

label1.grid(row=0, column=0, ipadx=10, ipady=10)
label2.grid(row=0, column=1, ipadx=20, ipady=20)
label3.grid(row=1, column=0, columnspan=2, ipadx=30, ipady=30)

root.mainloop()
