import random

turns_left = 3
while turns_left > 0:
    turns_left = turns_left - 1
    player = input("Pick (R)ock, (P)aper, or (S)cissors:")

    computer = random.randint(1, 3)
    if computer == 1:
        computer = "r"
    elif computer == 2:
        computer = "p"
    elif computer == 3:
        computer = "s"
    
    if (player == computer):
        print("It's a tie!")

    if player == "r":
        if computer == "s":
            print("Player wins! Rock breaks Scissors")
        else:
            print("Computer wins!")
    
    elif player == "p":
        if computer == "r":
            print("Computer wins!Paper covers Rock!")
        else:
            print("Player wins!")
          
    elif player == "s":
        if computer == "p":
            print("Player wins! Scissors cut Paper!")
        else:
            print("Computer wins!")
