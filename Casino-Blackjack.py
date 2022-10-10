# Casino Blackjack

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
from replit import clear

def tally(card_list):
    x = card_list.copy()
    for key in range(len(card_list)):
        if x[key] == 'J' or x[key] == 'Q' or x[key] == 'K':
            x[key] = 10
        elif x[key] == 'A':
            x[key] = 11
    for key in range(len(card_list)):    
        while sum(x) > 21:
            if x[key] == 11:
                x[key] = 1
                sum(x)
            else:
                break

            
    return sum(x)


def stand(card_list):
    global dealer_cards
    while tally(card_list) < 17:
        hit('Dealer')
    if tally(dealer_cards) == 21 and len(dealer_cards) == 2:
        score()
        print('Dealer opens blackjack. Dealer Wins.')
    elif tally(dealer_cards) <= 21 and tally(dealer_cards) > tally(player_cards):
        score()
        print('Dealer Wins.')
    elif tally(dealer_cards) == tally(player_cards):
        score()
        print('Push.')
    elif tally(dealer_cards) > 21:
        score()
        print('Dealer busts. Player Wins.')
    else:
        score()
        print('Player Wins.')

def hit(x):
    if x == 'Dealer':
        dealer_cards.append(random.choice(cards))
    elif x == 'Player':
        player_cards.append(random.choice(cards))

    
def score():
    print(f'\nYour cards: {player_cards}, current score: {tally(player_cards)}')
    print(f'Dealer shows {dealer_cards}\n')
    

print(logo)
game_start = input('\nDo you want to play a game of blackjack? \'y\' or \'n\': ')

while game_start == 'y':
    clear()
    print(logo)
    cards = [2,3,4,5,6,7,8,9,'J','Q','K','A']
    player_cards = []
    dealer_cards = []
    dealer_current = 0
    
    # Dealer given 1 card, Player given 2 cards
    hit('Dealer')
    hit('Player')
    hit('Player')

    # Tallying player score
    score()
    
    # Checking for blackjack
    if tally(player_cards) == 21:
        print('Blackjack! You Win.')
    else:
        # Player's Option
        while tally(player_cards) < 21 :
            player_choice = input('Type \'y\' to hit, type \'n\' to stand: ')
            if player_choice == 'y':
                hit('Player')
                score()
                tally(player_cards)
            elif player_choice == 'n':
                stand(dealer_cards)
                break
        # Player hits 21 and is forced to stand
        if tally(player_cards) == 21:
            stand(dealer_cards)
        # Player busts
        elif tally(player_cards) > 21:
            print('Player busts. Dealer Wins.')
        
    
    game_start = input('Do you want to play another game of blackjack? \'y\' or \'n\': ')

print('End')