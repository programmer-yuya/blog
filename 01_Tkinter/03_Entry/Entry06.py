import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Entry-完全独学Python")
root.geometry("500x300")

# ラベル
label = tk.Label(root, text="入力欄")
label.pack()

# 入力欄(Entry)の作成
entry = tk.Entry(root, cursor="circle")
entry.pack()

# ウィンドウの表示
root.mainloop()