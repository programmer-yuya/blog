# １つ選択出来るようにする
import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Radiobutton-完全独学Python")
root.geometry("500x300")

# 選択されたオプションを格納するための変数
selected_option = tk.StringVar(value=1)

# ラジオボタンの作成
radiobutton01 = tk.Radiobutton(root, text="ラジオボタン１", variable=selected_option, value="1")
radiobutton01.pack()

radiobutton02 = tk.Radiobutton(root, text="ラジオボタン２", variable=selected_option, value="2")
radiobutton02.pack()

radiobutton03 = tk.Radiobutton(root, text="ラジオボタン３", variable=selected_option, value="3")
radiobutton03.pack()

# ウィンドウの表示
root.mainloop()