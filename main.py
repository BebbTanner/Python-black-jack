'''
    What is the main gameplay loop for black jack?

    The player would be delt 2 starting cards.
    The player would then be given one of three options:
    hit
    fold
    stay

    If the player gets close to 21 the player wins.
    If the player goes over 21 they bust and lose.
    If the player does not go over 21 they have to compete with the house.
    If the house has the higher score without going over the house wins.

    I need the card values for each of the cards.
    If it is the first ace in your hand it counts as 11.
    If it is the second ace in your hand that second one is worth one point.

    What are the win conditions?
    What are the lose conditions?
    What conditions are needed to trigger the dealer phase?
    What conditions are needed to trigger the player phase?
'''

# Libraries
import random

random.seed()

randomNum1 = random.randint(1,11)
randomNum2 = random.randint(1,11)

playerHand = f"{randomNum1} {randomNum2}"
playerValue = randomNum1 + randomNum2

print(playerHand)
print("Would you like another card?")

playerChoice = input("What would you like to do(Hit, Fold, Stay): ")