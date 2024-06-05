import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Separator-完全独学Python")
root.geometry("300x200")

# 上部のラベルを作成
label1 = ttk.Label(root, text="上部のラベル", padding=10)
label1.pack(pady=10)

# セパレータを作成（水平）
separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', pady=10)

# 下部のラベルを作成
label2 = ttk.Label(root, text="下部のラベル", padding=10)
label2.pack(pady=10)

# セパレータを作成（垂直）
frame = ttk.Frame(root)
frame.pack(pady=10, expand=True, fill='both')

label3 = ttk.Label(frame, text="左のラベル", padding=10)
label3.pack(side='left', padx=10)

separator2 = ttk.Separator(frame, orient='vertical')
separator2.pack(side='left', fill='y', padx=10)

label4 = ttk.Label(frame, text="右のラベル", padding=10)
label4.pack(side='left', padx=10)

# メインループの実行
root.mainloop()
