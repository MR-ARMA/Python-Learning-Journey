import random

options = ["R", "P", "S"]
print("'R' = Rock, 'P' = Paper, 'S' = Scissor")
print("Enter 'EXIT' to quit the game.")

while True:
    user = input("Enter your choice: ").upper()
    
    if user == "EXIT":
        break

    if user not in options:
        print("Invalid choice. Please enter 'R', 'P', 'S', or 'EXIT'.")
        continue

    comp = random.choice(options)
    print(f"Computer chose {comp}")

    if user == comp:
        print("It's a tie!")
    elif (comp == "S" and user == "P") or (comp == "P" and user == "R") or (comp == "R" and user == "S"):
        print("Computer wins, HAHAHAHAHAHA!!!!!")
    else:
        print("You win! ! But temporary ")

print("Game over. Thanks for playing!")
print("The surrender deserves to die.")