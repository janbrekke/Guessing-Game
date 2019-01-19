import random

guessesused = int(0)

name = input("Well hello Stranger..\nWhat's your name? or should I call the \"Stranger Danger\" Hotline?\n")

number = random.randint(1, 100)
print("\n\nOkay sweet!\nLet's play a game "+name+"..\nI am thinking of a number between 1 and 100..\nNow it's your turn. What number am I thinking of?")

while True:
   try:
       guess = int(input("Number:    "))
       val = int(guess)
       
       
       guessesused += 1 
       
       if guess < number:
        print("NOPE! Too low..\n")

       if guess > number:
        print("NIX! You're too high..\n")

       if guess == number:
           break
       
   except ValueError:
        print("\nHEEEYYY!!!?\nThis AINT numbers!!\n")

if guess == number:
    guess = int(guessesused)
    print("\n\nWell Well Well "+name+"!\nIt looks like you guessed the magic number in",guessesused,"guesses!\n\n****** Congrats! ******")
