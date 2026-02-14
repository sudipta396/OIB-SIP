
while True:
    mass = float(input("Enter your mass in kg: "))
    height = float(input("Enter your height in meters: "))

    if mass <= 0 or mass >=300:
        print("Invalid input , please enter a valid weight !")
    elif height <= 0 or height > 2.5:
        print("Invalid input , please enter a valid height !")
    else:
        bmi = mass / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        print("\n----- BMI RESULT -----")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    choice = input("Do you want to Calculate again ?? (yes/no): ").lower()
    if choice == "no":
        break
