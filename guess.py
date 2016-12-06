# put this line at the start of your program
# to make the functions of this package available
import random
# creates a random number between 3 and 567 - edit as necessary
myNum = random.randint(1, 1000)
print("I'm thinking of a number between 1 and 1000. Enter your guess!")
guess = int(raw_input())
    
while guess != myNum:
  if guess > myNum:
    print("Nope, too high! Guess again.")
    guess= int(raw_input())
  if guess < myNum:
    print("Nope, too low! Guess again.")
    guess= int(raw_input())
  if guess == myNum:
    print("Hurray!! You guessed the right number!")
