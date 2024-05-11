import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.title("Label-完全独学Python")
root.geometry("600x300")

# Label（ラベル）の作成
font1 = ("MS明朝", 20, "bold", "italic", "underline", "overstrike")
label1 = tk.Label(root, text="完全独学Python", font=font1, fg="red")
label1.pack()

font2 = ("HGｺﾞｼｯｸE", 30,"italic", "underline")
label2 = tk.Label(root, text="みんなもPythonに挑戦しよう！", font=font2, fg="#6277fc")
label2.pack()

# ウィンドウの表示
root.mainloop()