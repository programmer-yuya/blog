import tkinter as tk

# メインウィンドウの作成
root = tk.Tk()
root.title("Message-完全独学Python")
root.geometry("500x300")

# メッセージウィジェットの作成
message = tk.Message(root, bg="green", text="これはTkinterのMessageウィジェットの例です。複数行のテキストを簡単に表示できます。")
message.pack()

# メインループの開始
root.mainloop()