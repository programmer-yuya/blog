import tkinter as tk

root = tk.Tk()
root.title("Place-完全独学Python")
root.geometry("500x300")

# ウィジェットの作成（カラフルなボタン）
button1 = tk.Button(root, text="Top Left", bg="lightblue")
button2 = tk.Button(root, text="Top Center", bg="lightgreen")
button3 = tk.Button(root, text="Top Right", bg="lightcoral")
button4 = tk.Button(root, text="Center", bg="lightyellow")
button5 = tk.Button(root, text="Bottom Left", bg="lightpink")
button6 = tk.Button(root, text="Bottom Right", bg="lightgray")

# ウィジェットの配置
button1.place(x=0, y=0, width=100, height=50, anchor='nw')           # 左上
button2.place(relx=0.5, y=0, width=100, height=50, anchor='n')       # 中央上
button3.place(relx=1.0, y=0, width=100, height=50, anchor='ne')      # 右上

button4.place(relx=0.5, rely=0.5, width=100, height=50, anchor='center')  # 中央

button5.place(x=0, rely=1.0, width=100, height=50, anchor='sw')      # 左下
button6.place(relx=1.0, rely=1.0, width=100, height=50, anchor='se') # 右下

# 追加の装飾
root.configure(bg="lightblue")  # 背景色の変更

# メインループの開始
root.mainloop()
