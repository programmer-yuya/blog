import tkinter as tk

root = tk.Tk()
root.title("Place Layout-完全独学Python")
root.geometry("300x200")

# ウィジェットを作成
label1 = tk.Label(root, text="Label 1", bg="red", fg="white")
label2 = tk.Label(root, text="Label 2", bg="blue", fg="white")
label3 = tk.Label(root, text="Label 3", bg="green", fg="white")

# ウィジェットを配置
label1.place(x=20, y=20, width=100, height=50)
label2.place(relx=0.5, rely=0.5, anchor="center")
label3.place(relx=0.5, y=100, anchor="n")

root.mainloop()