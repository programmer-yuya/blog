import tkinter as tk

root = tk.Tk()
root.title("Pack-完全独学Python")
root.geometry("500x300")

# ラベルの作成と配置
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# ボタンの作成と配置
button = tk.Button(root, text="Click Me")
button.pack()

root.mainloop()
