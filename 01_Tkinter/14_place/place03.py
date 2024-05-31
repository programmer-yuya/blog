import tkinter as tk

root = tk.Tk()
root.title("Place-完全独学Python")
root.geometry("500x300")

# ウィジェットの作成
label1 = tk.Label(root, text="Hello, World!", bg="lightblue")

# ウィジェットの配置
label1.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

root.mainloop()