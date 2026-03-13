import tkinter as tk
import random
import string

def password_generate():
    length = int(length_entry.get())

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)
    
    result_final.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

tk.Label(root,text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()

tk.Button(root,text="Generate Password",command=password_generate).pack()

result_final = tk.Label(root, text="")
result_final.pack()

root.mainloop()