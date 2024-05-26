# create_text
import tkinter as tk

root = tk.Tk()
root.title("Canvas-完全独学Python")
root.geometry("500x300")

# Canvasウィジェットの作成
canvas = tk.Canvas(root, width=200, height=200,bg="white", highlightthickness=0)
canvas.pack()

# テキストの描写
canvas.create_text(100, 20, text="Canvas Text")

# メインループの開始
root.mainloop()
