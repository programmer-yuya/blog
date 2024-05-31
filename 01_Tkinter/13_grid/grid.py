import tkinter as tk

root = tk.Tk()
root.title("Grid Layout Example")
root.geometry("400x300")

# ウィジェットの作成
label1 = tk.Label(root, text="Label 1", bg="lightblue")
label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label3 = tk.Label(root, text="Label 3", bg="lightcoral")
label4 = tk.Label(root, text="Label 4", bg="lightyellow")
label5 = tk.Label(root, text="Label 5", bg="lightgrey")
label_ipad = tk.Label(root, text="Internal Padding", bg="lightblue")

# フレームの作成
frame = tk.Frame(root, bg="lightgrey")
frame.grid(row=3, column=0, columnspan=3, sticky="nsew")

label_in = tk.Label(frame, text="Inside Frame", bg="lightgreen")

# ウィジェットの配置
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=0, column=1, padx=10, pady=10)
label3.grid(row=0, column=2, padx=10, pady=10)
label4.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
label5.grid(row=1, column=2, rowspan=2, padx=10, pady=10)
label_ipad.grid(row=2, column=0, ipadx=20, ipady=10, padx=10, pady=10)
label_in.grid(row=0, column=0, padx=10, pady=10)

# 行と列のサイズを設定
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()
