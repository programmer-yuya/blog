#複数グループ
import tkinter as tk

def display_selected_option():
    label01 = tk.Label(root, text="selected_option01：" + selected_option01.get())
    label01.pack()
    
    label02 = tk.Label(root, text="selected_option02：" + selected_option02.get())
    label02.pack()

# ウィンドウの作成
root = tk.Tk()
root.title("Radiobutton-完全独学Python")
root.geometry("500x300")

# 選択されたオプションを格納するための変数
selected_option01 = tk.StringVar(value=1)
selected_option02 = tk.StringVar(value=1)

# ラジオボタンの作成
radiobutton01_01 = tk.Radiobutton(root, text="ラジオボタン01_01", variable=selected_option01, value="1")
radiobutton01_01.pack()

radiobutton01_02 = tk.Radiobutton(root, text="ラジオボタン01_02", variable=selected_option01, value="2")
radiobutton01_02.pack()

radiobutton01_03 = tk.Radiobutton(root, text="ラジオボタン01_03", variable=selected_option01, value="3")
radiobutton01_03.pack()

radiobutton02_01 = tk.Radiobutton(root, text="ラジオボタン02_01", variable=selected_option02, value="1")
radiobutton02_01.pack()

radiobutton02_02 = tk.Radiobutton(root, text="ラジオボタン02_02", variable=selected_option02, value="2")
radiobutton02_02.pack()

radiobutton02_03 = tk.Radiobutton(root, text="ラジオボタン02_03", variable=selected_option02, value="3")
radiobutton02_03.pack()

# ボタンの作成
button = tk.Button(root, text="選択したオプションを表示", command=display_selected_option)
button.pack()

# ウィンドウの表示
root.mainloop()