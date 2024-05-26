# create_line
import tkinter as tk

root = tk.Tk()
root.title("Canvas-完全独学Python")
root.geometry("500x300")

# Canvasウィジェットの作成
canvas = tk.Canvas(root, width=200, height=200,bg="white", highlightthickness=0)
canvas.pack()

# 直線の描写
canvas.create_line(0, 0, 200, 200, fill="red")

# メインループの開始
root.mainloop()
