import tkinter as tk

root = tk.Tk()
root.title("Grid-完全独学Python")
root.geometry("500x300")

# ウィジェットの作成
label1 = tk.Label(root, text="Label 1", bg="lightblue")
label2 = tk.Label(root, text="Label 2", bg="lightgreen")

# ウィジェットの配置
label1.grid(row=1, column=1)
label2.grid(row=2, column=2)

# 行と列のサイズを設定（ウィンドウの中央に配置するため）
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)

root.mainloop()
