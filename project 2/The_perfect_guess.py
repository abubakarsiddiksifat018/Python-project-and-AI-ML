import random 

n = random.randint(1,100)

a = -1

guess = 1 # because if we correctly guess at 1st attempt . we already guessed once

while(n!=a) :
    a = int(input("guess the  number"))

    if(a > n ) : 
        print("Lower number please")
    elif(a < n):
         print("Higher number please")
    guess+=1

print(f"You have correctly guesses {n} in {guess} guesses")