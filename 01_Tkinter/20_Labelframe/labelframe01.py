import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Labelframe-完全独学Python")
root.geometry("400x200")

# Labelframeの作成
labelframe = ttk.Labelframe(root, text="完全独学Python", padding=(10, 5))
labelframe.pack(padx=10, pady=10, fill="both", expand=True)

# ラベルとエントリーの作成
label = ttk.Label(labelframe, text="Labelframeの中のウィジェットです！")
label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

# メインループの実行
root.mainloop()