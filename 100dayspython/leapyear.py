#Leap Year python mini project 
year = int ( input("please Enter a Year"))

if year % 4==0:
    if year %100==0:
        if year%400==0:
            print(f"{year} is Leap Year")
        else:
            print(f"{year} is Not Leap year")
    else:
        print(f"{year} is Leap Year")
else:
    print("Not a Leap year")