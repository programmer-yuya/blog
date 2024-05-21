import tkinter as tk

# メインウィンドウの作成
root = tk.Tk()
root.title("Message-完全独学Python")
root.geometry("500x300")

# メッセージウィジェットの作成
# （フォント, サイズ, 太さ, 斜体, 下線, 打消し線）
font = ("MS明朝", 10, "bold", "italic", "underline", "overstrike")
message = tk.Message(root, font=font,width=200, text="これはTkinterのMessageウィジェットの例です。複数行のテキストを簡単に表示できます。")
message.pack()

# メインループの開始
root.mainloop()