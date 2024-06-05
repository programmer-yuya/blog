import tkinter as tk
from tkinter import ttk
import time

def start_progress():
    progress.start()

    # 進捗バーが一定時間進行します
    for i in range(101):
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.05)

    # 進捗バーを停止します
    progress.stop()

# メインウィンドウの作成
root = tk.Tk()
root.title("Progressbar-完全独学Python")
root.geometry("300x100")

# Progressbarの作成
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)

# Startボタンの作成
start_button = ttk.Button(root, text="Start Progress", command=start_progress)
start_button.pack()

# メインループの実行
root.mainloop()
