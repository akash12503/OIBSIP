try:
    weight = float(input("Enter the Weight in kg:"))
    height = float(input("Enter the Height in m:"))

    if weight <= 0 or height <= 0:
        print("Error : Enter the positive values")
    else:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "underweight"
        elif bmi < 25:
            category = "Normalweight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "obesity range"

        print(f"\n Your BMI is : {bmi:.2f}")
        print(f"Adult reference category :",category)
        print("Note : BMI categories are general adult references,not medical diagnosis")
except ValueError:
    print("Error : Please enter the number only")
