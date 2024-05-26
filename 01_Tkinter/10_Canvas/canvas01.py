import tkinter as tk

def draw_circle(event):
    x, y = event.x, event.y
    r = 10  # 円の半径
    canvas.create_oval(x-r, y-r, x+r, y+r, fill="blue")

root = tk.Tk()
root.title("Canvas-完全独学Python")

# Canvasウィジェットの作成
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# マウスクリックイベントのバインド
canvas.bind("<Button-1>", draw_circle)

# メインループの開始
root.mainloop()
