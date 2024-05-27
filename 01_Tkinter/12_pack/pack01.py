import tkinter as tk

root = tk.Tk()
root.title("Pack-完全独学Python")
root.geometry("500x300")

label_top = tk.Label(root, text="Top Label")
label_top.pack(side=tk.TOP)

label_bottom = tk.Label(root, text="Bottom Label")
label_bottom.pack(side=tk.BOTTOM)

label_left = tk.Label(root, text="Left Label")
label_left.pack(side=tk.LEFT)

label_right = tk.Label(root, text="Right Label")
label_right.pack(side=tk.RIGHT)

root.mainloop()