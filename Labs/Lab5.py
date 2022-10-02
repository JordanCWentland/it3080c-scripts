# Lab 5 Number guessing game! 
# By Jordan Wentland (Wentlajc)
import random 
x=True
y=True
computer = random.randint(1,100)
print("Welcome to the random Guessing Game!\nIn this game, you will attempt to guess the number the computer is thinking of.\nIf the number is too high or low, it will tell you.\nGood Luck!")
while x == True: 
    guess = int(input("Please enter your guess between 1 and 100: "))
    diff = computer-guess
    if diff==0:
        print("You guessed the number! Thanks for playing!")
        x=False
    elif diff<0:
        print("your guess is too high, please try again!")
    elif diff>0:
        print("Your guess is too low, please try again!")