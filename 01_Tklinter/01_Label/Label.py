import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Label-完全独学Python")
root.geometry("500x300")

# Label（ラベル）の作成
label1 = tk.Label(root, text="完全独学Python", fg="red")
label1.pack()

label2 = tk.Label(root, text="みんなもPythonに挑戦しよう！", fg="#3632a8")
label2.pack()


# ウィンドウの表示
root.mainloop()