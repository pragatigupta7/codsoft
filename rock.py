import random
point_user = 0
point_computer = 0

while True:
    user_input = input("enter you choice (rock ,paper, scrissors)")
    possible_choice = ["rock,paper,scissors"]
    computer_input = random.choice(possible_choice)

    print(f"You chose {user_input}, computer chose{computer_input}")

    if user_input == computer_input:
     print("Its a Draw as both selected {user_input}")
    elif user_input == "rock":
        if computer_input == "scissors":
            print("User wins, Rock will break the scissors")
            point_user += 1
        else:
            print("User lose,paper will cover rock")
            point_user += 1

    elif user_input == "paper":
     if computer_input == "rock":
        print("User wins, paper will cover rock")
        point_user += 1
     else:
        print("User lose,scissors will cut the paper")
        point_user += 1
    elif user_input == "scissors":
        if computer_input == "paper":
            print("User wins,scissors will cut the paper")
            point_user += 1
    else:
        print("User lose,rock will break the scissors")
        point_user += 1

    play_again = input("Do you want to play again? (y/n):")
    if play_again.lower() != "y":
        break

print(f"Total points are: user {point_user} Computer: {point_computer}")
print("Game Over")