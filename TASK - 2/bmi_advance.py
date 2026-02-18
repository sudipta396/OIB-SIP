import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    mass = float(weight_user.get())
    height = float(height_user.get())

    if mass <= 0 or mass >=300:
        messagebox.showerror("Invalid input , please enter a valid weight !")
        return
    elif height <= 0 or height > 2.5:
        messagebox.showerror("Invalid input , please enter a valid height !")
        return
    bmi = mass / (height ** 2)

    if bmi < 18.5:
            category = "Underweight"
    elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
    elif 25 <= bmi < 29.9:
            category = "Overweight"
    else:
        category = "Obese"

    result_user.config(text= f"BMI is : {bmi:.2f} \nWeight Categorie is :{category}")


root = tk.Tk()
root.title('BMI Calculator')
root.geometry("400x350")


tk.Label(root,text="Enter your Weight(kg)").pack(pady=4)
weight_user = tk.Entry(root)
weight_user.pack()

tk.Label(root,text="Enter your Height(m)").pack(pady=4)
height_user = tk.Entry(root)
height_user.pack()

tk.Button(root, text = "Calculate your BMI" ,command=calculate_bmi).pack(pady=9)

result_user = tk.Label(root,text="")
result_user.pack(pady=9)

root.mainloop()


