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

    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        hand.append(card)
    return hand


def display():
    pass


def hit(hand):
    card = deck.pop()
    hand.append(card)
    return hand


def stick():
    pass


def bust(dealer_hand, player_hand):
    pass


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
    print()
    if score(dealer_hand) >= score(player_hand):
        print('Unlucky, Dealer won this hand')
        return True
    elif score(dealer_hand) < score(player_hand):
        print('Congratulations, You won this hand!')
        return True
    else:
        return False


def dealer_rules():
    pass


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def game_state(dealer_hand, player_hand):
    print(f'Dealer: {dealer_hand[0][0]} of {dealer_hand[0][1].capitalize()}, __________')
    print(f'Your Score: {score(dealer_hand)}\n')
    print(f'You: {player_hand[0][0]} of {player_hand[0][1].capitalize()}, {player_hand[1][0]} of {player_hand[1][1].capitalize()}')
    print(f'Your Score: {score(player_hand)}\n')


def play():
    clear()
    print('Welcome to Blackjack!\n')
    dealer_hand = deal()
    player_hand = deal()
    game_state(dealer_hand, player_hand)
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
            game_state(dealer_hand, player_hand)
        elif choice.lower()[0] == 's':
            win_check(dealer_hand, player_hand)
            pass
        # else do a try loop
        # Once stand then dealer plays
        # win_check()
        # play_again()
    pass


def play_again():
    pass

if __name__ == "__main__":
    play()
