import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Frame-完全独学Python")
root.geometry("500x300")

# フレームの作成
frame = tk.Frame(root, width="100", height="400", bd=2, bg="red", relief=tk.RAISED)
frame.propagate(False)
frame.pack()

# フレーム内用のラベル
label = tk.Label(frame, text="完全独学Python")
label.pack()


# ウィンドウの表示
root.mainloop()