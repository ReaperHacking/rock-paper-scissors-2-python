#Rock, Paper, and Scissors, against a computer!
import random

print("Welcome to the second rock, paper, and scissors game on my github!\n")

#Makes Computer Function and choose random choice!
rps = ["rock", "paper", "scissors"]
computer_choice = random.choice(rps)

#Function very similar to the other game, making user and computer fight eachother!
def rock_paper_scissors2(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("TIE!")
    elif user_choice.lower() == 'rock' and computer_choice.lower() == 'scissors':
        print("USER WINS! (ROCK SMASHES SCISSORS! MAAAAAYHEM!!!)\n")
    elif user_choice.lower() == 'scissors' and computer_choice.lower() == 'rock':
        print("COMPUTER WINS! (ROCK SMASHES SCISSORS! MAAAAAYHEM!!!)\n")
    elif user_choice.lower() == 'paper' and computer_choice.lower() == 'rock':
        print("USER WINS! (PAPER SUFFOCATES ROCK! FAAAAATALITY!!!)\n")
    elif user_choice.lower() == 'rock' and computer_choice.lower() == 'paper':
        print("COMPUTER WINS! (PAPER SUFFOCATES ROCK! FAAAAATALITY!!!)\n")
    elif user_choice.lower() == 'scissors' and computer_choice.lower() == 'paper':
        print("USER WINS! (SCISSORS SLAUGHTERS PAPER! BRUUUUUTALITY!!!)\n")
    elif user_choice.lower() == 'paper' and computer_choice.lower() == 'scissors':
        print("COMPUTER WINS! BRUUUUUUTALITY!!!\n")
    else:
        print("ERROR, TRY AGAIN!")

#While loop to ask if the user would like to keep playing!
while True:
    user_choice = input("Enter a choice! (Rock, Paper, Scissors.): ").lower()
    rock_paper_scissors2(user_choice, computer_choice)
    choice2 = input("Keep playing? (Yes/No)")
    if choice2.lower() == "no":
        break



