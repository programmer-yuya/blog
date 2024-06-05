import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def on_item_selected(event):
    selected_item = tree.selection()[0]
    item = tree.item(selected_item)
    messagebox.showinfo("選択された項目", f"Name: {item['text']}\nAge: {item['values'][0]}\nCountry: {item['values'][1]}")

# ウィンドウの作成
root = tk.Tk()
root.title("Treeview-完全独学Python")
root.geometry("500x300")

# Treeviewの作成
tree = ttk.Treeview(root, selectmode="browse")

# カラムの設定
tree["columns"] = ("one", "two")
tree.column("#0", width=150, minwidth=150, stretch=tk.NO)
tree.column("one", width=100, minwidth=100, stretch=tk.NO)
tree.column("two", width=100, minwidth=100, stretch=tk.NO)

# カラムの見出し設定
tree.heading("#0", text="Name", anchor=tk.W)
tree.heading("one", text="Age", anchor=tk.W)
tree.heading("two", text="Country", anchor=tk.W)

# サンプルデータの挿入
tree.insert("", "end", text="John Doe", values=("25", "USA"))
tree.insert("", "end", text="Anna Smith", values=("30", "UK"))
tree.insert("", "end", text="Peter Brown", values=("28", "Canada"))

# イベントハンドリングの設定
tree.bind("<<TreeviewSelect>>", on_item_selected)

# Treeviewの配置
tree.pack(pady=20)

# メインループの開始
root.mainloop()
