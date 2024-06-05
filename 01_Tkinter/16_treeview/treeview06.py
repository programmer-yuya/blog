import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Treeview Show Option Example")
root.geometry("500x300")

# デフォルトのTreeviewウィジェットの作成
tree = ttk.Treeview(root, columns=("one", "two", "three"), show="tree headings")

# カラムの設定
tree.column("#0", width=150, minwidth=150)
tree.column("one", width=100, minwidth=50)
tree.column("two", width=100, minwidth=50)
tree.column("three", width=100, minwidth=50)

# ヘッディングの設定
tree.heading("#0", text="Name", anchor=tk.W)
tree.heading("one", text="Column 1", anchor=tk.W)
tree.heading("two", text="Column 2", anchor=tk.W)
tree.heading("three", text="Column 3", anchor=tk.W)

# サンプルデータの挿入
tree.insert("", "end", text="Item 1", values=("Value 1", "Value 2", "Value 3"))
tree.insert("", "end", text="Item 2", values=("Value A", "Value B", "Value C"))

# Treeviewの配置
tree.pack(pady=20, padx=20, fill="both", expand=True)

# showオプションの変更を確認するためのボタン
def show_tree():
    tree.configure(show="tree")

def show_headings():
    tree.configure(show="headings")

def show_tree_headings():
    tree.configure(show="tree headings")

def hide_all():
    tree.configure(show="")

# ボタンの作成と配置
btn_show_tree = tk.Button(root, text="Show Tree", command=show_tree)
btn_show_tree.pack(side="left", padx=5, pady=5)

btn_show_headings = tk.Button(root, text="Show Headings", command=show_headings)
btn_show_headings.pack(side="left", padx=5, pady=5)

btn_show_tree_headings = tk.Button(root, text="Show Tree & Headings", command=show_tree_headings)
btn_show_tree_headings.pack(side="left", padx=5, pady=5)

btn_hide_all = tk.Button(root, text="Hide All", command=hide_all)
btn_hide_all.pack(side="left", padx=5, pady=5)

# メインループの開始
root.mainloop()
