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

name_frame = tk.Frame(root)
name_label = tk.Label(name_frame, text="名前:")
name_entry = tk.Entry(name_frame)

age_frame = tk.Frame(root)
age_label = tk.Label(age_frame, text="年齢:")
age_entry = tk.Entry(age_frame)

gender_frame = tk.Frame(root)
gender_label = tk.Label(gender_frame, text="性別:")
gender_var = tk.StringVar(value="男性")
male_radio = tk.Radiobutton(gender_frame, text="男性", variable=gender_var, value="男性")
female_radio = tk.Radiobutton(gender_frame, text="女性", variable=gender_var, value="女性")
other_radio = tk.Radiobutton(gender_frame, text="その他", variable=gender_var, value="その他")

feedback_frame = tk.Frame(root)
feedback_label = tk.Label(feedback_frame, text="フィードバック:")
feedback_text = tk.Text(feedback_frame, height=10, width=40)

submit_button = tk.Button(root, text="送信", command=submit)

# ウィジェットの配置
title_label.pack(pady=20)

name_frame.pack(anchor="w", padx=50, pady=5)
name_label.pack(side="left")
name_entry.pack(side="left", padx=20, fill="x", expand=True)

age_frame.pack(anchor="w", padx=50, pady=5)
age_label.pack(side="left")
age_entry.pack(side="left", padx=20, fill="x", expand=True)

gender_frame.pack(anchor="w", padx=50, pady=5)
gender_label.pack(side="left")
male_radio.pack(side="left", padx=10)
female_radio.pack(side="left", padx=10)
other_radio.pack(side="left", padx=10)

feedback_frame.pack(anchor="w", padx=50, pady=5)
feedback_label.pack(anchor="w")
feedback_text.pack(anchor="w", padx=20, pady=10)

submit_button.pack(pady=20)

# メインループの開始
root.mainloop()
