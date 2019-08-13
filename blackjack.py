import random
import os


# suits
suit = ['diamonds', 'clubs', 'spades', 'hearts']

# cards and their respective values
card = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}

deck = []
for s in suit:
    for c in card:
        deck.append((c, s))


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def deal():
    hand = []
    random.shuffle(deck)
    for i in range(2):
        hand.append(deck.pop())
    return hand


def display():
    pass


def hit(hand):
    return hand.append(deck.pop())


def stand(player_hand):
    pass


def bust_check(hand):
    return score(hand) > 21


def score(hand):
    """
    Make a count ace function because at the moment it rounds down for every value if there is one ace in the list
    """
    score = 0
    for h in hand:
        score += card[h[0]]
        for i in range(len(hand)):
            if score > 21 and hand[i][0] == 'Ace':
                score -= 10
    return score


def split():
    pass


def blackjack(hand):
    for m in range(len(hand)):
        if hand[m][0] == 'Ace':
            for n in range(len(hand)):
                if hand[n][0] == 'King' or hand[n][0] == 'Queen' or hand[n][0] == 'Jack':
                    return True



def win_check(dealer_hand, player_hand):
    pass


def dealer_turn(dealer_hand, player_hand):
    pass


def player_turn(dealer_hand, player_hand):
    choice = input('Hit or Stick? ')
    while choice.lower()[0] == 'h':
        hit(player_hand)
        game_state(dealer_hand, player_hand)

        choice = input('Hit or Stick? ')
    return player_hand


def game_state(dealer_hand, player_hand):
    print()

    print(f'Dealers Hand:', end=" ")
    for i in range(len(dealer_hand)-1):
        print(f'{dealer_hand[0][0]} of {dealer_hand[0][1].capitalize()}', end=", ")
    print('__________')
    print(f'Dealer Score: {score(dealer_hand)}\n')

    print('Your Hand:', end=" ")
    for i in range(len(player_hand)):
        print(f'{player_hand[i][0]} of {player_hand[i][1].capitalize()}', end=", ")
    print(f'\nYour Score: {score(player_hand)}\n')


def play():
    clear()
    dealer_hand = deal()
    player_hand = deal()
    game_state(dealer_hand, player_hand)
    if blackjack(dealer_hand):
        print('Dealer has blackjack')
        exit()
    player_turn(dealer_hand, player_hand)



def play_again():
    pass

if __name__ == "__main__":
    play()
