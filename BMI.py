weight=float(input("Enter your weight."))
height=float(input("Ehter your height."))
bmi=weight/height**2
if bmi < 18.5:
    print("You are under weight.")
elif 18.5 <= bmi < 25:
    print("Your weight is normal.")
elif 25 <= bmi < 30:
    print("You are over weight.")
else:
    print("You are obese.")
    