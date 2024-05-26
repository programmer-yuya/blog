# create_rectangle
import tkinter as tk

root = tk.Tk()
root.title("Canvas-完全独学Python")
root.geometry("500x300")

# Canvasウィジェットの作成
canvas = tk.Canvas(root, width=200, height=200,bg="white", highlightthickness=0)
canvas.pack()

# 長方形の描写
canvas.create_rectangle(20, 20, 180, 180, outline="green")

# メインループの開始
root.mainloop()
