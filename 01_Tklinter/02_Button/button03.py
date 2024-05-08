import tkinter as tk

# ボタンを押したらラベルの値を更新する
def change_label():
    label_text.set("ボタン押しました！")

# ウィンドウの作成
root = tk.Tk()
root.title("Button-完全独学Python")
root.geometry("500x300")

# ラベルに表示するテキストの設定
label_text = tk.StringVar()
label_text.set("ボタンを押してください")

# ラベルの作成
label = tk.Label(root, textvariable=label_text)
label.pack()

# ボタンの作成
button = tk.Button(root, text="ボタン", bg="red", activebackground="#3632a8",command=change_label)
button.pack()

root.mainloop()