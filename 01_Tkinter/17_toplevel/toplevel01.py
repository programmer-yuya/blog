import tkinter as tk

# メインウィンドウの作成
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

def open_toplevel():
    # 新しいToplevelウィンドウの作成
    toplevel = tk.Toplevel(root)
    toplevel.title("Toplevel Window")
    toplevel.geometry("300x200+500+500")

    # ラベルの追加
    label = tk.Label(toplevel, text="これはToplevelウィンドウです")
    label.pack(pady=20)

    # 閉じるボタンの追加
    close_button = tk.Button(toplevel, text="閉じる", command=toplevel.destroy)
    close_button.pack(pady=10)

# ボタンの作成
open_button = tk.Button(root, text="Toplevelを開く", command=open_toplevel)
open_button.pack(pady=20)

# メインループの開始
root.mainloop()
