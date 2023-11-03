from art import logo
print(logo)


def add (n1,n2):
    return n1+n2
def subtract (n1,n2):
    return n1-n2
def multiply (n1,n2):
    return n1*n2
def divide (n1,n2):
    return n1/n2


opearation ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1 = int(input("please enter the first number? "))
num2 = int(input("please enter the second number? "))
for operator in opearation:
    print(operator)
operator_symbole = input("pick a  symbole from line above!")
calculation_fucntion = opearation[operator_symbole]
answer=calculation_fucntion(num1,num2)
print(f"{num1} {operator_symbole} {num2} = {answer}")