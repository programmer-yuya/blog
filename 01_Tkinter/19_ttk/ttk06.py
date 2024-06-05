import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Sizegrip-完全独学Python")
root.geometry("300x200")

# ラベルを作成
label = ttk.Label(root, text="右下隅のサイズ変更グリップを試してみてください。", padding=20)
label.pack(expand=True)

# Sizegripの作成
sizegrip = ttk.Sizegrip(root)
sizegrip.pack(side="right", anchor="se")

# メインループの実行
root.mainloop()
