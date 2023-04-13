import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. \n"))

computer_choice = random.randint(0, 2)
print(f"Computer chose '{computer_choice}'")

if user_choice > 2 or user_choice < 0:
    print("You typed an invalid number, you lose!")

elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
