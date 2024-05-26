import tkinter as tk

root = tk.Tk()
root.title("Grid Layout-完全独学Python")
root.geometry("250x200")

# ウィジェットを作成
label1 = tk.Label(root, text="Label 1", bg="red", fg="white", width=20)
label2 = tk.Label(root, text="Label 2", bg="blue", fg="white")
label3 = tk.Label(root, text="Label 3", bg="green", fg="white")
entry1 = tk.Entry(root)

# ウィジェットを配置
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=0, column=1, padx=10, pady=10)
label3.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
entry1.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

root.mainloop()