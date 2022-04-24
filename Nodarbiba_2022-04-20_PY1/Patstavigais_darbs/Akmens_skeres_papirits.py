#variables
choices = {
  0: "Rock",
  1: "Paper",
  2: "Scissors",
}

for choice_number, choice_name in choices.items():
    print(f"{choice_number} ==> {choice_name}")
    
#generating number    
import random
computer_choice = random.randint(0, 2)

#user input
user_choice = int(input("Your turn:"))

#check if entered number is in scope
if user_choice <= 2:
    print(choices[computer_choice], "vs", choices[user_choice])

    #calculations
    if (computer_choice == 2 and user_choice == 1) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 0 and user_choice == 2):
        print("Computer wins this round!")
    elif computer_choice == user_choice:
        print("No winners this time!")
    else:
        print("You won!")
else:
    print("Wrong input!")        