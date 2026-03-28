import random
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)

while player not in options:
    player = input("enter a choice:")

print(f"Player: {player}")
print(f"Computer: {computer}")

if player == computer:
    print("tie")

elif player == "rock" and computer == "scissors":
    print("you won!!")
elif player == "paper" and computer == "rock":
    print("you won!")
elif player == "scissors" and computer == "paper":
    print("you won!")

else:
    print("you lost!")