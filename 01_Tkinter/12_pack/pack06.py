import tkinter as tk

root = tk.Tk()
root.title("Pack-完全独学Python")
root.geometry("500x300")

# 上部中央に配置 (デフォルト)
label_center = tk.Label(root, text="Center (default)", bg="lightblue")
label_center.pack(anchor=tk.CENTER, pady=10)

# 左上に配置
label_nw = tk.Label(root, text="NW (North West)", bg="lightgreen")
label_nw.pack(anchor=tk.NW, pady=10)

# 右上に配置
label_ne = tk.Label(root, text="NE (North East)", bg="lightcoral")
label_ne.pack(anchor=tk.NE, pady=10)

# 左下に配置
label_sw = tk.Label(root, text="SW (South West)", bg="lightyellow")
label_sw.pack(anchor=tk.SW, pady=10)

# 右下に配置
label_se = tk.Label(root, text="SE (South East)", bg="lightgrey")
label_se.pack(anchor=tk.SE, pady=10)

root.mainloop()
