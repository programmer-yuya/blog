import tkinter as tk

def  get_selected_value():
    # 選択した選択肢のインデックスを取得
    selected_index = listbox.curselection()
    
    # 選択した値を表示するラベル
    for v in selected_index:
        label = tk.Label(root, text=listbox.get(v))
        label.pack()
    

# ウィンドウの作成
root = tk.Tk()
root.title("Listbox-完全独学Python")
root.geometry("500x300")

# リストボックスの中身
colors = ["red", "blue", "green"]
var_listbox = tk.StringVar(value=colors)
# リストボックスの作成
listbox = tk.Listbox(root, listvariable=var_listbox, selectmode=tk.SINGLE)
# 選択肢の追加
listbox.insert(tk.END, "black")
# 選択肢の削除
listbox.delete(1, 3)
# リストボックスの配置 
listbox.pack()

# ボタンの作成
button = tk.Button(root, text="リストから取得", command=get_selected_value)
button.pack()

# ウィンドウの表示
root.mainloop()