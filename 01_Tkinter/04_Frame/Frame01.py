import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Frame-完全独学Python")
root.geometry("500x300")

# フレームの作成
frame = tk.Frame(root, width="400", height="100", bd=2, bg="red", relief=tk.RAISED)
frame.propagate(True)
frame.pack()

# フレーム内用のラベル
label = tk.Label(frame, text="フレーム内に表示する時は、frameオブジェクトを渡そう")
label.pack()


# ウィンドウの表示
root.mainloop()