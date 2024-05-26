# create_oval
import tkinter as tk

root = tk.Tk()
root.title("Canvas-完全独学Python")
root.geometry("500x300")

# Canvasウィジェットの作成
canvas = tk.Canvas(root, width=200, height=200,bg="white", highlightthickness=0)
canvas.pack()

# 楕円の描写
canvas.create_oval(20, 20, 180, 100, width=5)

# メインループの開始
root.mainloop()
