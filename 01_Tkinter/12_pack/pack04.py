import tkinter as tk

root = tk.Tk()
root.title("Pack-完全独学Python")
root.geometry("500x300")

# padxのみを指定
label_padx = tk.Label(root, text="Padding X", bg="lightblue")
label_padx.pack(padx=20)

# padyのみを指定
label_pady = tk.Label(root, text="Padding Y", bg="lightgreen")
label_pady.pack(pady=20)

# 両方を指定
label_padx_pady = tk.Label(root, text="Padding X and Y", bg="lightcoral")
label_padx_pady.pack(padx=20, pady=20)

root.mainloop()
