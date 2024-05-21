# 選択肢した値の取得
import tkinter as tk

def display_selected_option():
    label = tk.Label(root, text="selected_option：" + selected_option.get())
    label.pack()

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

# ボタンの作成
button = tk.Button(root, text="選択したオプションを表示", command=display_selected_option)
button.pack()

# ウィンドウの表示
root.mainloop()