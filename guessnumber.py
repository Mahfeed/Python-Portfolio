import random 
number= random.randint(1,100)
guess =  0 
for i in range(5):
    guess = int(input(f"Attempt {i+1}/5||Enter the guessed number:"))
    if guess==number :
        print("You Won!")
        break 
    elif(guess<number):
        print("Guess Higher")
    else: print("Guess Lower") 
else:
    print(f"You are out of chances! The Number was {number}")

