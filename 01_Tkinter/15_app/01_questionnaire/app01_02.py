import tkinter as tk
from tkinter import messagebox


def submit():
    # 入力内容を取得
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    feedback = feedback_text.get("1.0", tk.END).strip()
    
    # 必須項目が空かどうかチェック
    if not name or not age or not gender or not feedback:
        messagebox.showerror("入力エラー", "全ての項目を入力してください。")
        return
    
    # 入力内容を表示
    messagebox.showinfo("入力内容", f"名前: {name}\n年齢: {age}\n性別: {gender}\nフィードバック:\n{feedback}")

# ウィンドウの作成
root = tk.Tk()
root.title("アンケート-完全独学Python")
root.geometry("500x500")

# ウィジェットの作成
title_label = tk.Label(root, text="アンケートフォーム", font=("Arial", 16))

name_label = tk.Label(root, text="名前:")
name_entry = tk.Entry(root)

age_label = tk.Label(root, text="年齢:")
age_entry = tk.Entry(root)

gender_label = tk.Label(root, text="性別:")
gender_var = tk.StringVar(value="男性")
male_radio = tk.Radiobutton(root, text="男性", variable=gender_var, value="男性")
female_radio = tk.Radiobutton(root, text="女性", variable=gender_var, value="女性")
other_radio = tk.Radiobutton(root, text="その他", variable=gender_var, value="その他")

feedback_label = tk.Label(root, text="フィードバック:")
feedback_text = tk.Text(root, height=10, width=40)

submit_button = tk.Button(root, text="送信", command=submit)

# ウィジェットの配置
title_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
name_entry.grid(row=1, column=1, padx=10, pady=5)

age_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
age_entry.grid(row=2, column=1, padx=10, pady=5)

gender_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)
male_radio.grid(row=3, column=1, sticky="w", padx=10)
female_radio.grid(row=4, column=1, sticky="w", padx=10)
other_radio.grid(row=5, column=1, sticky="w", padx=10)

feedback_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)
feedback_text.grid(row=6, column=1, padx=10, pady=5)

submit_button.grid(row=7, column=0, columnspan=2, pady=20)

# メインループの開始
root.mainloop()
