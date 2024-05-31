import tkinter as tk


# ボタンを押すと、チェックボックスの状態を表示する
def display_state_checkbox():
    # 状態を表示するラベルを作成
    label_state = tk.Label(root, text=state_checkbox.get())
    label_state.pack()
    

# ウィンドウの作成
root = tk.Tk()
root.title("Checkbox-完全独学Python")
root.geometry("500x300")

# チェックボックスの状態を格納する変数
state_checkbox = tk.BooleanVar()

# チェックボックスの作成
checkbox = tk.Checkbutton(root, text="選択肢１", variable=state_checkbox)
checkbox.pack()

# ボタンの作成
button = tk.Button(root, text="push", command=display_state_checkbox)
button.pack()

print(type(state_checkbox.get()))

# ウィンドウの表示
root.mainloop()
