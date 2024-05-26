import tkinter as tk

root = tk.Tk()
root.title("Layout-完全独学Python")
root.geometry("500x300")

# ウィジェットを作成
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="blue", fg="white")
label3 = tk.Label(root, text="Label 3", bg="green", fg="white")

# ウィジェットを配置
label1.pack(side="top", fill="x")
label2.pack(side="left", fill="y")
label3.pack(side="right", fill="y")

root.mainloop()