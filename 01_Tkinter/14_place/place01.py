import tkinter as tk

root = tk.Tk()
root.title("Place-完全独学Python")
root.geometry("500x300")

# ウィジェットの作成
label1 = tk.Label(root, text="Hello, World!", bg="lightblue")

# ウィジェットの配置
label1.place(x=100, y=100, width=200, height=50)

root.mainloop()