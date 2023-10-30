print("Welcome to BMI Calculator")
height = float(input("Please Enter Your Height in M : "))
weight = float(input("Please Enter Your Weight in KG : "))
bmi = weight / (height*height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are under Weight")
elif bmi <25 :
    print(f"Your BMI is {bmi}, You have normal weight") 
else:
    print("you are over weighted !")