import tkinter as tk

# メインウィンドウの作成
root = tk.Tk()
root.title("Message-完全独学Python")
root.geometry("500x300")

# メッセージウィジェットの作成
message01 = tk.Message(root, justify="left",width=200, text="これはTkinterのMessageウィジェットの例です。複数行のテキストを簡単に表示できます。")
message01.pack()

message02 = tk.Message(root, justify="center",width=200, text="これはTkinterのMessageウィジェットの例です。複数行のテキストを簡単に表示できます。")
message02.pack()

message03 = tk.Message(root, justify="right",width=200, text="これはTkinterのMessageウィジェットの例です。複数行のテキストを簡単に表示できます。")
message03.pack()

# メインループの開始
root.mainloop()