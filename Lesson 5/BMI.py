# BMI checker

w = float(input("enter the weight of the person in kgs : "))
h = float(input("enter the height of the person in metres : "))

bmi = w/(h * h)

if bmi < 18.4:
    print("Your bmi is",bmi)
    print("you are underweight")
elif bmi < 25:
    print("Your bmi is",bmi)
    print("you are Healthy")
elif bmi < 30:
    print("Your bmi is",bmi)
    print("you are over Weight")
else:
    print("Your bmi is",bmi)
    print("you are Obese")