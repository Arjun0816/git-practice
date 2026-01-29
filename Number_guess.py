import random
number = random.randint(1,10)
guess = 0
while guess != number:
    guess = int(input("enter a number between 1 and 10 : "))
    if guess < number:
        print("guess is low")
    elif guess > number:
        print("guess is high")
    else:
        print("congrats, your guess is correct")
