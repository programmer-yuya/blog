# width,height
import tkinter as tk

root = tk.Tk()
root.title("Canvas-完全独学Python")
root.geometry("500x300")

# Canvasウィジェットの作成
canvas = tk.Canvas(root, width=200, height=200,bg="white")
canvas.pack()

# メインループの開始
root.mainloop()
