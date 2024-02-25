import random
play = True
while play:
    a = ["rock", "paper", "sissor"]
    user = input("Enter your move: ").lower()
    computer = random.choice(a)
    print(f"User entered {user} and opponent entered {computer}")
    if user == "rock" and computer == "sissor":
        print("You won. Rock broke sissor")
    elif user == "rock" and computer == "paper":
        print("You loose. Rock is defeted by paper")
    elif user == "paper" and computer == "sissor":
        print("You loose.Sissor cuts paper")
    elif user == "paper" and computer == "rock":
        print("You loose.sissor cuts paper")
    elif user == "sissor" and computer == "rock":
        print("You loose.Rock broke sissor")
    elif user == "sissor" and computer == "paper":
        print("You won.Sissor cuts paper")
    elif user == computer:
        print(f"Its a draw . Both was {user}")
    else:
        print("error in the input")

    a = input("Do you want to play the Rock paper sissor game :(y or n)").lower()
    if a == "y":
        play = True
    if a == "n":
        play = False
