import tkinter as tk

root = tk.Tk()
root.title("Pack-完全独学Python")
root.geometry("500x300")

# ラベルの作成と配置（横方向に広がる）
label_fill_x = tk.Label(root, text="Fill X", bg="lightblue")
label_fill_x.pack(fill=tk.X, padx=5, pady=5)

# ラベルの作成と配置（縦方向に広がる）
label_fill_y = tk.Label(root, text="Fill Y", bg="lightgreen", height=5)
label_fill_y.pack(fill=tk.Y, padx=5, pady=5)

# ラベルの作成と配置（両方向に広がる）
label_fill_both = tk.Label(root, text="Fill Both", bg="lightcoral")
label_fill_both.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()