import tkinter as tk

root = tk.Tk()
root.title("Pack-完全独学Python")
root.geometry("500x300")

# ラベルの作成と配置（expandを指定しない場合）
label_no_expand = tk.Label(root, text="No Expand", bg="lightblue")
label_no_expand.pack(fill=tk.BOTH, padx=5, pady=5)

# ラベルの作成と配置（expand=True）
label_expand = tk.Label(root, text="Expand", bg="lightgreen")
label_expand.pack(fill=tk.BOTH, expand=False, padx=5, pady=5)

root.mainloop()