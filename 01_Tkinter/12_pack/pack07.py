import tkinter as tk

root = tk.Tk()
root.title("Pack-完全独学Python")
root.geometry("500x300")

# 背景をカラフルにするためにフレームを使用
frame_top = tk.Frame(root, bg="skyblue")
frame_bottom = tk.Frame(root, bg="lightgrey")

frame_top.pack(fill=tk.BOTH, expand=True)
frame_bottom.pack(fill=tk.BOTH, expand=True)

# 上部フレームに配置されるラベル
label_top_left = tk.Label(frame_top, text="Top Left", bg="lightgreen")
label_top_left.pack(side=tk.LEFT, padx=20, pady=10, anchor=tk.NW)

label_top_center = tk.Label(frame_top, text="Top Center", bg="lightcoral")
label_top_center.pack(side=tk.TOP, padx=10, pady=10, anchor=tk.N)

label_top_right = tk.Label(frame_top, text="Top Right", bg="lightyellow")
label_top_right.pack(side=tk.RIGHT, padx=20, pady=10, anchor=tk.NE)

# 下部フレームに配置されるラベル
label_bottom_left = tk.Label(frame_bottom, text="Bottom Left", bg="lightblue")
label_bottom_left.pack(side=tk.LEFT, padx=20, pady=10, anchor=tk.SW)

label_bottom_center = tk.Label(frame_bottom, text="Bottom Center", bg="lightpink")
label_bottom_center.pack(side=tk.BOTTOM, padx=10, pady=10, anchor=tk.S)

label_bottom_right = tk.Label(frame_bottom, text="Bottom Right", bg="lightgrey")
label_bottom_right.pack(side=tk.RIGHT, padx=20, pady=10, anchor=tk.SE)

root.mainloop()
