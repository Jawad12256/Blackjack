import random

#init deck
deck = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']*4

#numerical value of each card (ace adjusted for later)    
vals = {'A':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        '10':10,
        'J':10,
        'Q':10,
        'K':10}

#return value of cards in hand, or best value within 21 if there is an ace
def handValue(cards):
    #if ace in hand
    if 'A' in cards:
        total = 0
        for x in cards:
            total += vals[x]
        for c in cards:
            if total <= 11 and c == 'A':
                total += 10
        return total
    #if no ace in hand
    else:
        total = 0
        for x in cards:
            total += vals[x]
        return total

#draw a card, removing it from the deck list
def drawCard():
    card = deck.pop(random.randint(0,len(deck)-1))
    return card

#init variables and hands
comhand = [drawCard(),drawCard()]
myhand = [drawCard(),drawCard()]
comstick = False
mystick = False
combust = False
mybust = False
validChoices = ['t','s','twist','stick']

gameContinue = True
while gameContinue:
    #my turn
    
    if (not mystick) and (not mybust):
        print('Your hand:')
        print(myhand)
        choice = 'none'
        #cannot stick under 16
        if handValue(myhand) < 16 and (not mystick) and (not mybust):
            #twist
            confirm = input('Your only choice is to twist. Press enter to twist.')
            myhand.append(drawCard())
            print('You drew a ' + myhand[-1])
        else:
            while choice.lower() not in validChoices:
                choice = str(input('Twist or stick?'))
                if choice.lower() == 'twist' or choice.lower() == 't':
                    #twist
                    print('Twisting...')
                    myhand.append(drawCard())
                    print('You drew a ' + myhand[-1])
                elif choice.lower() == 'stick' or choice.lower() == 's':
                    #stick
                    print('Sticking...')
                    mystick = True
                else:
                    #invalid input
                    print('Invalid input. Please try again.')
        if handValue(myhand) > 21:
            #bust, terminate game
            mybust = True
            gameContinue = False

    #com turn
    
    #cannot stick under 16
    if handValue(comhand) < 16 and (not comstick) and (not combust):
        #twist
        print('Computer chose to twist...')
        comhand.append(drawCard())
    elif (not comstick) and (not mybust):
        choice = random.choice(validChoices)
        if choice.lower() == 'twist' or choice.lower() == 't':
            #twist
            print('Computer chose to twist...')
            comhand.append(drawCard())
        elif choice.lower() == 'stick' or choice.lower() == 's':
            #stick
            print('Computer chose to stick...')
            comstick = True
    if handValue(comhand) > 21:
        #bust, terminate game
        combust = True
        gameContinue = False
    #check gamestate
    if mybust or combust or (mystick and comstick):
        gameContinue = False

if combust: #computer bust, player wins
    print('The computer went bust.')
    print('You Win!')
elif mybust: #player bust, computer wins
    print('You went bust.')
    print('Computer Wins.')
else:
    if handValue(myhand) > handValue(comhand): #player has higher score, player wins
        print(f"You-Computer : {handValue(myhand)}-{handValue(comhand)}")
        print('You Win!')
    elif handValue(comhand) > handValue(myhand): #computer has higher score, computer wins
        print(f"You-Computer : {handValue(myhand)}-{handValue(comhand)}")
        print('Computer Wins.')
    else: #identical scores
        print('Draw!')
