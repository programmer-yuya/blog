import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Notebook-完全独学Python")
root.geometry("500x300")

# Notebookウィジェットの作成
notebook = ttk.Notebook(root)

# タブ1の作成
frame1 = ttk.Frame(notebook, width=500, height=300)
frame1.pack(fill='both', expand=True)
notebook.add(frame1, text='Tab 1')

# タブ2の作成
frame2 = ttk.Frame(notebook, width=500, height=300)
frame2.pack(fill='both', expand=True)
notebook.add(frame2, text='Tab 2')

# タブ3の作成
frame3 = ttk.Frame(notebook, width=500, height=300)
frame3.pack(fill='both', expand=True)
notebook.add(frame3, text='Tab 3')

# Notebookの表示
notebook.pack(expand=True, fill='both')

# タブ1にウィジェットを追加
label1 = ttk.Label(frame1, text="これはタブ1です", padding=20)
label1.pack()

# タブ2にウィジェットを追加
label2 = ttk.Label(frame2, text="これはタブ2です", padding=20)
label2.pack()

# タブ3にウィジェットを追加
label3 = ttk.Label(frame3, text="これはタブ3です", padding=20)
label3.pack()

# メインループの実行
root.mainloop()
