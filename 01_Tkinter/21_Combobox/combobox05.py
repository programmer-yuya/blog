import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox- textvariableオプション")
root.geometry("300x200")

# 選択された値を保持する変数
selected_value = tk.StringVar()

# Comboboxの作成
options = ["Option 1", "Option 2", "Option 3"]
combobox = ttk.Combobox(root, values=options, textvariable=selected_value)
combobox.pack(padx=10, pady=10)

# 選択された値を表示するためのラベル
selected_label = ttk.Label(root, text="Selected: ")
selected_label.pack(padx=10, pady=10)

def show_selected():
    selected_label.config(text=f"Selected: {combobox.get()}")

# 値を表示するボタンの作成
show_button = ttk.Button(root, text="Show Selected", command=show_selected)
show_button.pack(padx=10, pady=10)

root.mainloop()
