import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



choice = int(input("What do you choos ? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
computer_choice= random.randint(0,2)
#print(computer_choice)
if choice <0 or choice >=2:
    print("Invalide number! You lose")
else:
    if choice ==0 and computer_choice==2:
        print("You Win!")
    elif computer_choice >choice:
        print("Computer Wins!")
    elif computer_choice == choice:
        print("Match draw!")
