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

import random

random.seed()

'''
    Maybe the playerHand should be an array instead that can have more random numbers put into it.

    Ok so this generates two random numbers between 1 and 11, but now I need to find away to allow the user to generate another number and then add that number to the array.
'''
playerHand = [random.randint(1,11) for _ in range(2)]
handValue = sum(playerHand)

'''
    This will generate a new card that I am going to add to the playerHand array.

    This whole thing stops after one choice I think that I need to put it in a do-while loop.
'''
newCard = random.randint(1,11)

print(playerHand)
print(handValue)

playerChoice = input("Would you like another card?(Y or N): ")

if handValue <= 21:
    if playerChoice == 'Y' or playerChoice == 'y':
        playerHand.append(newCard)
        
        print("\nNew Hand: ", playerHand)
        print("New value: ", sum(playerHand))

elif handValue > 21:
    print("You lost!")



# print("Would you like another card?")
# playerChoice = input("What would you like to do(Hit, Fold, Stay): ")