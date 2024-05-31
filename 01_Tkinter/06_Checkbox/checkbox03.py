import tkinter as tk


# ボタンを押すと、チェックボックスの状態を表示する
def display_state_checkbox():
    # 状態を表示するラベルを作成
    label_state01 = tk.Label(root, text="選択肢１：" + str(state_checkbox01.get()))
    label_state02 = tk.Label(root, text="選択肢２：" + str(state_checkbox02.get()))
    label_state03 = tk.Label(root, text="選択肢３：" + str(state_checkbox03.get()))
    
    label_state01.pack()
    label_state02.pack()
    label_state03.pack()
    

# ウィンドウの作成
root = tk.Tk()
root.title("Checkbox-完全独学Python")
root.geometry("500x300")

# チェックボックスの状態を格納する変数
state_checkbox01 = tk.BooleanVar()
state_checkbox02 = tk.BooleanVar()
state_checkbox03 = tk.BooleanVar()

# 初期値の設定
state_checkbox01.set(True)

# チェックボックスの作成
checkbox01 = tk.Checkbutton(root, text="選択肢１", variable=state_checkbox01, bg="red", width=5, height=2)
checkbox01.pack()
checkbox02 = tk.Checkbutton(root, text="選択肢２", variable=state_checkbox02, bg="#6bff93", width=15, height=3)
checkbox02.pack()
checkbox03 = tk.Checkbutton(root, text="選択肢３", variable=state_checkbox03, bg="green", width=25, height=5)
checkbox03.pack()

# ボタンの作成
button = tk.Button(root, text="push", command=display_state_checkbox)
button.pack()

# ウィンドウの表示
root.mainloop()
