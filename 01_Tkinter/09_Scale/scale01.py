import tkinter as tk

def update_color(r, g, b):
    color = f"#{r:02x}{g:02x}{b:02x}"
    canvas.config(bg=color)

def on_scale_r(val):
    r = int(val)
    g = scale_g.get()
    b = scale_b.get()
    update_color(r, g, b)

def on_scale_g(val):
    r = scale_r.get()
    g = int(val)
    b = scale_b.get()
    update_color(r, g, b)

def on_scale_b(val):
    r = scale_r.get()
    g = scale_g.get()
    b = int(val)
    update_color(r, g, b)

root = tk.Tk()
root.title("RGBカラー調整")

# スケールの作成
scale_r = tk.Scale(root, from_=0, to_=255, orient=tk.HORIZONTAL, label="Red", command=on_scale_r)
scale_r.pack()
scale_g = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Green", command=on_scale_g)
scale_g.pack()
scale_b = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Blue", command=on_scale_b)
scale_b.pack()

# キャンバスの作成
canvas = tk.Canvas(root, width=200, height=200, bg="#000000")
canvas.pack()

# メインループの開始
root.mainloop()