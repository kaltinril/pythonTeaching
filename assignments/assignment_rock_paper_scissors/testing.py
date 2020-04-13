import random

computer_wins = 0
player_wins = 0
while computer_wins < 2 and player_wins < 2:
    choice = input("Pick R, P, or S")
    # have computer pick random number 1, 2, 3
    computer = random.randint(1, 3)

    # Check who wins
    if choice == "R" and computer == 2:
        print("computer's paper covers rock")
        computer_wins = computer_wins + 1
    elif choice == "R" and computer == 1:
        print("Rock and rock, tie !")
    elif choice == "R" and computer == 3:
        print("Rock smashes computer's sisscors")
        player_wins = player_wins + 1

# Print out who won the game (Use the bigger value)

