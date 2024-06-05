import tkinter as tk
from tkinter import ttk

def calculate_total():
    quantity_value = quantity.get()
    price_value = price.get()
    total_value = quantity_value * price_value
    result_label.config(text=f"Total: {total_value:.2f}")

# メインウィンドウの作成
root = tk.Tk()
root.title("Spinbox-完全独学Python")
root.geometry("500x300")

# 数量入力のSpinbox
quantity_label = ttk.Label(root, text="Quantity:")
quantity_label.pack(pady=5)

quantity = tk.IntVar(value=1)
quantity_spinbox = tk.Spinbox(root, from_=1, to=10, textvariable=quantity)
quantity_spinbox.pack(pady=5)

# 価格入力のSpinbox
price_label = ttk.Label(root, text="Price:")
price_label.pack(pady=5)

price = tk.DoubleVar(value=0.99)
price_spinbox = tk.Spinbox(root, from_=0.99, to=9.99, increment=0.50, textvariable=price, format="%.2f")
price_spinbox.pack(pady=5)

# Calculateボタン
calculate_button = ttk.Button(root, text="Calculate", command=calculate_total)
calculate_button.pack(pady=20)

# 結果表示用のラベル
result_label = ttk.Label(root, text="")
result_label.pack(pady=20)

# メインループの開始
root.mainloop()
