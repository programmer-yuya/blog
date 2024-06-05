import tkinter as tk
from tkinter import ttk

# メインウィンドウの作成
root = tk.Tk()
root.title("Treeview-完全独学Python")
root.geometry("700x400")

# スタイルの設定
style = ttk.Style()
style.theme_use("clam")

# Treeviewヘッダのスタイル設定
style.configure("Treeview.Heading", 
                font=("Helvetica", 12, "bold"), 
                background="#4caf50", 
                foreground="white")

# Treeviewのスタイル設定
style.configure("Treeview",
                font=("Helvetica", 10),
                rowheight=25,
                fieldbackground="white",
                background="white",
                foreground="black")

# スクロールバーのスタイル設定
style.configure("Vertical.TScrollbar", 
                gripcount=0,
                background="gray",
                darkcolor="gray",
                lightcolor="gray",
                troughcolor="white",
                bordercolor="gray",
                arrowcolor="white")

# Treeviewウィジェットの作成
tree = ttk.Treeview(root, style="Treeview")

# カラムの設定
tree["columns"] = ("Name", "Age", "Email")
tree.column("#0", width=0, stretch=tk.NO)  # 隠すための設定
tree.column("Name", anchor=tk.W, width=200)
tree.column("Age", anchor=tk.CENTER, width=100)
tree.column("Email", anchor=tk.W, width=300)

# ヘッディングの設定
tree.heading("#0", text="", anchor=tk.W)  # 隠すための設定
tree.heading("Name", text="名前", anchor=tk.W)
tree.heading("Age", text="年齢", anchor=tk.CENTER)
tree.heading("Email", text="メールアドレス", anchor=tk.W)

# サンプルデータの挿入
data = [
    ("山田 太郎", 28, "taro.yamada@example.com"),
    ("鈴木 次郎", 34, "jiro.suzuki@example.com"),
    ("佐藤 三郎", 45, "saburo.sato@example.com"),
    ("高橋 四郎", 22, "shiro.takahashi@example.com"),
    ("伊藤 五郎", 30, "goro.ito@example.com"),
    ("山田 太郎", 28, "taro.yamada@example.com"),
    ("鈴木 次郎", 34, "jiro.suzuki@example.com"),
    ("佐藤 三郎", 45, "saburo.sato@example.com"),
    ("高橋 四郎", 22, "shiro.takahashi@example.com"),
    ("伊藤 五郎", 30, "goro.ito@example.com"),
    ("山田 太郎", 28, "taro.yamada@example.com"),
    ("鈴木 次郎", 34, "jiro.suzuki@example.com"),
    ("佐藤 三郎", 45, "saburo.sato@example.com"),
    ("高橋 四郎", 22, "shiro.takahashi@example.com"),
    ("伊藤 五郎", 30, "goro.ito@example.com"),
    ("山田 太郎", 28, "taro.yamada@example.com"),
    ("鈴木 次郎", 34, "jiro.suzuki@example.com"),
    ("佐藤 三郎", 45, "saburo.sato@example.com"),
    ("高橋 四郎", 22, "shiro.takahashi@example.com"),
    ("伊藤 五郎", 30, "goro.ito@example.com"),
]

for i, (name, age, email) in enumerate(data):
    tree.insert("", "end", iid=i, values=(name, age, email))

# Treeviewとスクロールバーの配置
tree.pack(pady=20, padx=20, fill="both", expand=True)

# スクロールバーの設定
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview, style="Vertical.TScrollbar")
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# メインループの開始
root.mainloop()
