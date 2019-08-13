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


player_hand = []
dealer_hand = []


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
    if score(hand) > 21:
        return True


def score(hand):
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
    if score(dealer_hand) >= score(player_hand):
        print('Unlucky, Dealer won this hand')
        return True
    elif score(dealer_hand) < score(player_hand):
        print('Congratulations, You won this hand!')
        return True
    else:
        return False


def dealer_turn(dealer_hand, player_hand):
    if bust_check(player_hand):
        print('Dealer won!')
        return
    elif score(dealer_hand) >= score(player_hand):
        print('Dealer won!')
    else:
        while score(dealer_hand) < 17:
            hit(dealer_hand)
            if bust_check(dealer_hand):
                print('You won! Dealer Bust')
            elif score(dealer_hand) >= score(player_hand):
                print('Dealer won!')


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def player_turn():
    pass


def start_game_state(dealer_hand, player_hand):
    print()
    print(f'Dealer: {dealer_hand[0][0]} of {dealer_hand[0][1].capitalize()}, __________')
    print(f'Your Score: {score(dealer_hand)}\n')
    print(f'You: {player_hand[0][0]} of {player_hand[0][1].capitalize()}, {player_hand[1][0]} of {player_hand[1][1].capitalize()}')
    print(f'Your Score: {score(player_hand)}\n')


def play():
    clear()
    print('Welcome to Blackjack!\n')
    dealer_hand = deal()
    player_hand = deal()
    start_game_state(dealer_hand, player_hand)
    if blackjack(player_hand):
        print('You got blackjack!')
        choice = True
    elif blackjack(dealer_hand):
        print('Dealer got blackjack!')
        choice = True
    else:
        choice = False
    if choice == False:
        choice = input('Do you want to Hit or Stand? ')
        if choice.lower()[0] == 'h':
            hit(player_hand)
            start_game_state(dealer_hand, player_hand)
        elif choice.lower()[0] == 's':
            stand(player_hand)
            start_game_state(dealer_hand, player_hand)
            # win_check(dealer_hand, player_hand)
            dealer_turn(dealer_hand, player_hand)
            pass


def play_again():
    pass

if __name__ == "__main__":
    play()
