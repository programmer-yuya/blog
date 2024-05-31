import tkinter as tk

root = tk.Tk()
root.title("Main Window")

toplevel = tk.Toplevel(root)
toplevel.title("Modal Window")
toplevel.transient(root)  # Toplevelウィンドウを親ウィンドウに設定

root.mainloop()
