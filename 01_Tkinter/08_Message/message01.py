import tkinter as tk

# メインウィンドウの作成
root = tk.Tk()
root.title("Message-完全独学Python")
root.geometry("500x300")

# メッセージウィジェットの作成
message = tk.Message(root, text="これはTkinterのMessageウィジェットの例です。複数行のテキストを簡単に表示できます。")
message.pack()

# ラベルの作成
label = tk.Label(root, text="これはTkinterのLabelウィジェットの例です。1行のテキストを簡単に表示できます。")
label.pack()

# メインループの開始
root.mainloop()