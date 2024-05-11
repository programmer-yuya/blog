import tkinter as tk

# ボタンを押下 → 入力されたテキストでラベルを作成・表示
def display_text():
    label_entry_text = tk.Label(root, text=entry.get())
    label_entry_text.pack()

# ウィンドウの作成
root = tk.Tk()
root.title("Entry-完全独学Python")
root.geometry("500x300")

# ラベル
label = tk.Label(root, text="入力欄")
label.pack()

# 入力欄(Entry)の作成
entry = tk.Entry(root)
entry.pack()

# ボタン
button = tk.Button(root, text="PUSH", command=display_text)
button.pack()

# ウィンドウの表示
root.mainloop()