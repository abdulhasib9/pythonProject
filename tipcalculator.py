#python mini project the tip calculator 
print("Welcome to tip calculator")
#amount of bill
bill =float(input("please enter the amount of bill $ ?"))
tip = float(input("what percentage of tip? 10, 12, 15?"))
people = int(input("please enter the amount of people to splite bill with : "))
bill_with_tip = tip/100*bill +bill
print(bill_with_tip)

bill_per_person = round(bill/people,2)
print(f"amount per person {bill_per_person}")
