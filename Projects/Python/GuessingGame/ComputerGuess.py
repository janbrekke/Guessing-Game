import random
import time
import sys

def computer_type(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

times = int(0)

print("Well hello Stranger..\nWant to play a game with the computer?\nLet's think of a number between 1 and 100, and have the computer guess it shall we?\n")

while True:
    try:
        secretnr = int(input("\nMy secret number is::    "))
        
        while True:
            if int(secretnr) < 0:
                print("*"*30)
                print("\nLower that 0 Ey??\nWise guy are we..??\nHMMM????")
                secretnr = ("wrong")
                break

            if int(secretnr) > 100:
                print("*"*30)
                print("\nAbove 100 eyh??\nCan't follow instructions there stranger..??\nHMMM????\nLet's try that again shall we?")
                secretnr = ("wrong")
                break
            else:
                break

        val = int(secretnr)
        break
    except ValueError:
        print("\nThis AINT the numbers i asked for!!\n")
        print("*"*30)

number = int(secretnr) 
print("*"*30,"\nHey Computer?!\nAre you ready??\n\n")
time.sleep(2)
computer_type("Hey stranger!\n")
time.sleep(1)
computer_type("I sure am ready!\n")
time.sleep(1)
computer_type("I really hope this is a hard one, because i'm really good at guessing numbers :P\n")
print("*"*30)
time.sleep(3)
print("You may start when ready\n")
time.sleep(3)
computer_type("\nOkay here i go in..\n")
computer_type("3\n")
time.sleep(1.5)
computer_type("2\n")
time.sleep(1.5)
computer_type("1\n")
time.sleep(1.5)
computer_type("....GO!\n")

guess = random.randint(1, 100)

while guess != secretnr:
    times += 1

    if guess > secretnr:
        guess -= 1
        guess = random.randint(1, guess)

    else:
        guess += 1
        guess = random.randint(guess, 100)
    print ("Hmm.. i wonder if", guess,"is the correct number?")

print("*"*30)
computer_type("Hey, wait?! could that be the correct number??\n")
time.sleep(2)
computer_type("YAY!! I got it!!\nSee, I told you i was good at this!!\n")
time.sleep(3)
print("\n\nWell Well Well Missy!\nIt looks like you guessed the magic number in",times,"guesses!\n\n****** Congrats! ******")
