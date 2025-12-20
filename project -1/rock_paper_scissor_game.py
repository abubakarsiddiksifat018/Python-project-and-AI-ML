'''
1 for rock
0 for paper
-1 for scissors
'''
# import random to let computer choose one of them 
import random 
computer = random.choice([-1, 0, 1])

youstr = input("enter your choice")

# creating dictionary storing values
youDict = {
    "r": 1,
    "p": 0,
    "s": -1
}

# reversing dictionary 
reverseDict = {
    1: "rock",
    0: "paper",
    -1: "scissor"
}

you = youDict[youstr]  # accessing values

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if (computer == you):
    print("its a draw")

else:
    if (computer == 1 and you == -1):
        print("You lose!")

    elif (computer == -1 and you == 1):
        print("you win!")

    elif (computer == 1 and you == 0):                   
        print("you win")

    elif (computer == 0 and you == 1):
        print("You lose!")

    elif (computer == 1 and you == 1):
        print("you win!")

    elif (computer == -1 and you == 0):
        print("you win!")

    elif (computer == 0 and you == -1):
        print("You lose!")

    else:
        print("invalid input")
 