import random as rd
deck = ['A', 'K', 'Q', 'J', '10','9','8','7','6','5','4','3','2',
'A', 'K', 'Q', 'J', '10','9','8','7','6','5','4','3','2',
'A', 'K', 'Q', 'J', '10','9','8','7','6','5','4','3','2',
'A', 'K', 'Q', 'J', '10','9','8','7','6','5','4','3','2']
print(len(deck))


total = 1000

def deal(deck): 
    playerhand = []
    dealerhand = []
    card1,card2 = rd.sample(deck, 2)
    deck.remove(card1)
    deck.remove(card2)
    playerhand.extend([card1, card2])
    dealer1,dealer2 = rd.sample (deck,2)
    deck.remove(dealer1)
    deck.remove(dealer2)
    dealerhand.extend([dealer1, dealer2])
    return deck,playerhand, dealerhand

def points(card1, card2):
    value = 0
    if card1.isdigit() == True:
        value += int(card1)
    else:
        if card1 == 'A':
            if value + 11 > 21:
                value += 1
            else:
                value += 11
        else:
            value += 10

    if card2.isdigit() == True:
        value += int(card2)
    else:
        if card2 == 'A':
            if value + 11 > 21:
                value += 1
            else:
                value += 11
        else:
            value += 10
    
    return value

def hit(deck,handtotal):
    card = rd.choice(deck)
    deck.remove(card)
    totalvalue = points(str(handtotal),card)
    return deck, totalvalue, card


def bj(deck, user_decision):
    #'deck' is a list with card values in string format
    
    deck,playerhand, dealerhand = deal(deck)
    playertotal = points(playerhand[0], playerhand[1])
    dealertotal = points(dealerhand[0], dealerhand[1]) 

    while True:
        decision = input(f"\nYour hand is: {playerhand}. Your total is: {playertotal}. The dealer has a {dealerhand[0]} and another hidden card. Would you like to hit or stand? \n")
        if decision == 'hit':
            deck, playertotal, hitcard = hit(deck, playertotal)
            playerhand.append(hitcard)
            if playertotal > 21:
                print(f'You drew a {playerhand[-1]}, bringing your total up to {playertotal}. You busted! \n')
                return False
        elif decision == 'stand':
            while dealertotal < 17:
                deck, dealertotal,hitcard = hit(deck, dealertotal)
                dealerhand.append(hitcard)
            if dealertotal > 21:
                print(f'The dealer busted with a total of {dealertotal} and a hand of {dealerhand}! You Won! \n' )
                return True
            print(f"Your hand was {playerhand} and the dealer's hand was {dealerhand}. You had a total of {playertotal} versus the dealer's {dealertotal} \n")
            if playertotal > dealertotal:
                print('You won!')
                return True
            elif playertotal < dealertotal:
                print('You lost!')
                return False
            else:
                print('You tied!')
                return 'tie'
        elif decision == 'end':
            return None
        else:
            print('Please put in either hit or stand!')

def user_decision(playerhand, playertotal, dealerhand):
    decision = input(f"\nYour hand is: {playerhand}. Your total is: {playertotal}. The dealer has a {dealerhand[0]} and another hidden card. Would you like to hit or stand? \n")
    return decision


'''
if condition == a:
    function(A)
elif condition == b:
    function(B)

if bet <= balance and bet > 0:
    bj
elif 

'''
def test_function(playerhand, dealerhand, decision):
    round_running = True
    result = None
    while round_running == True:
        if decision == 'hit':
            deck, playertotal, hitcard = hit(deck, playertotal)
            playerhand.append(hitcard)
            if playertotal > 21:
                print(f'You drew a {playerhand[-1]}, bringing your total up to {playertotal}. You busted! \n')
                result = False
                round_running = False
            round_running = False
        elif decision == 'stand':
            while dealertotal < 17:
                deck, dealertotal,hitcard = hit(deck, dealertotal)
                dealerhand.append(hitcard)
            if dealertotal > 21:
                print(f'The dealer busted with a total of {dealertotal} and a hand of {dealerhand}! You Won! \n' )
                result = True
                round_running = False
            print(f"Your hand was {playerhand} and the dealer's hand was {dealerhand}. You had a total of {playertotal} versus the dealer's {dealertotal} \n")
            if playertotal > dealertotal:
                print('You won!')
                result = True
                round_running = False
            elif playertotal < dealertotal:
                print('You lost!')
                result = False
                round_running = False
            else:
                print('You tied!')
                result = 'tie'
                round_running = False
        elif decision == 'end':
            result = None
            round_running = False
        else:
            print('Please put in either hit or stand!')
            round_running = False

    return result



while True:
    print(f'Your current balance is ${total}. \n')
    bet = input('How much do you want to bet? $')
    if total <= 0:
        print('You lost all your money!')
        break
    elif bet == 'end':
        break

    
    if float(bet) > total:
        print('Please put in a valid amount! \n')
    else:
        result = bj(bet,deck)
        if result == 'tie':
            result = bj(bet,deck)
        elif result == True:
            total += float(bet)*1.5
        elif result == False:
            total -= float(bet)
        elif result == None:
            break
        print(f'Your total is ${total}.')