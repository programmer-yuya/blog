import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Frame-完全独学Python")
root.geometry("500x300")

# フレームの作成
frame = tk.Frame(root, width="400", height="100", bd=10, bg="#6bff93", relief=tk.RAISED)
frame.propagate(False)
frame.pack()

# フレーム内用のラベル
label = tk.Label(frame, text="完全独学Python")
label.pack()


# ウィンドウの表示
root.mainloop()