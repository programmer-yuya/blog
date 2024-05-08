import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Label-完全独学Python")
root.geometry("500x300")

# Label（ラベル）の作成
label1 = tk.Label(root, text="完全独学Python", bg="red")
label1.pack()

label2 = tk.Label(root, text="みんなもPythonに挑戦しよう！", bg="#6277fc")
label2.pack()


# ウィンドウの表示
root.mainloop()