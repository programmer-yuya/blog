import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Button-完全独学Python")
root.geometry("500x300")

# ボタンの作成
button_flat = tk.Button(root, text="FLAT", relief=tk.FLAT)
button_flat.pack(pady=5)

# ボタンの作成
button_raised = tk.Button(root, text="RAISED", relief=tk.RAISED)
button_raised.pack(pady=5)

# ボタンの作成
button_sunken = tk.Button(root, text="SUNKEN", relief=tk.SUNKEN)
button_sunken.pack(pady=5)

# ボタンの作成
button_groove = tk.Button(root, text="GROOVE", relief=tk.GROOVE)
button_groove.pack(pady=5)

# ボタンの作成
button_ridge = tk.Button(root, text="RIDGE", relief=tk.RIDGE)
button_ridge.pack(pady=5)

# ボタンの作成
button_solid = tk.Button(root, text="SOLID", relief=tk.SOLID)
button_solid.pack(pady=5)

root.mainloop()