
from random import choice

#
# USER SELECTION
#


VALID_OPTIONS = ["rock", "paper", "scissors"]
u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in VALID_OPTIONS:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

c = choice(VALID_OPTIONS)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock":
    if c == "rock":
        print("Oh, it's a tie.")
    elif c == "paper":
        print("Oh, the computer won. It's ok.")
    elif c == "scissors":
        print("Oh, you won! Nice job.")
elif u == "paper":
    if c == "rock":
        print("Oh, you won! Nice job.")
    elif c == "paper":
        print("Oh, it's a tie.")
    elif c == "scissors":
        print("Oh, the computer won. It's ok.")
elif u == "scissors":
    if c == "rock":
        print("Oh, the computer won. It's ok.")
    elif ce == "paper":
        print("Oh, you won! Nice job.")
    elif c == "scissors":
        print("Oh, it's a tie.")
else:
    print("OOPS, SOMETHING WENT WRONG. Please try again.")