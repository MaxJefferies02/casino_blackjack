from random import shuffle
import os
import time

# define the card ranks, and suits
ranks = [_ for _ in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
symbols = ['♠', '♥', '♦', '♣']


def get_deck():
    """Return a new deck of cards."""
    return [[rank, suit] for rank in ranks for suit in suits]

# get a deck of cards, and randomly shuffle it
deck = get_deck()
shuffle(deck)


def reshuffle():
    deck = get_deck()
    shuffle(deck)


def hit(hand):
    new_player_card = deck.pop()
    hand.append(new_player_card)


def ascii_display(hand):
    lines = [[] for i in range(11)]
    for card in hand:
        if card[0] == 'Jack' or card[0] == 'Queen' or card[0] == 'King' or card[0] == 'Ace':
            label = card[0].rstrip('ackuening')
            space = ' '
        elif card[0] == 10:
            label = '10'
            space = ''
        else:
            label = card[0]
            space = ' '
        if card[1] == 'Spades':
            symbol = '♠'
        elif card[1] == 'Hearts':
            symbol = '♥'
        elif card[1] == 'Diamonds':
            symbol = '♦'
        elif card[1] == 'Clubs':
            symbol = '♣'
        lines[0].append('┌─────────┐')
        lines[1].append(f'│ {label}{space}      │')
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│         │')
        lines[5].append(f'│    {symbol}    │')
        lines[6].append('│         │')
        lines[7].append('│         │')
        lines[8].append('│         │')
        lines[9].append(f'│      {space}{label} │')
        lines[10].append('└─────────┘')
    for i in range(11):
        for x in range(len(lines[i])):
            if i == 9 and x == len(lines[i])-1:
                print(lines[i][x], end=' Hand')
            else:
                print(lines[i][x], end='')
        print()


def ascii_display_dealer(hand):
    lines = [[] for i in range(11)]
    if len(hand) == 2:
        if hand[0][0] == 'Jack' or hand[0][0] == 'Queen' or hand[0][0] == 'King' or hand[0][0] == 'Ace':
            label = hand[0][0].rstrip('ackuening')
            space = ' '
        elif hand[0][0] == 10:
            label = '10'
            space = ''
        else:
            label = hand[0][0]
            space = ' '
        if hand[0][1] == 'Spades':
            symbol = '♠'
        elif hand[0][1] == 'Hearts':
            symbol = '♥'
        elif hand[0][1] == 'Diamonds':
            symbol = '♦'
        elif hand[0][1] == 'Clubs':
            symbol = '♣'
        lines[0].append('┌─────────┐')
        lines[1].append(f'│ {label}{space}      │')
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│         │')
        lines[5].append(f'│    {symbol}    │')
        lines[6].append('│         │')
        lines[7].append('│         │')
        lines[8].append('│         │')
        lines[9].append(f'│      {space}{label} │')
        lines[10].append('└─────────┘')
        lines[0].append('┌─────────┐')
        lines[1].append('│░░░░░░░░░│')
        lines[2].append('│░░░░░░░░░│')
        lines[3].append('│░░░░░░░░░│')
        lines[4].append('│░░░░░░░░░│')
        lines[5].append('│░░░░░░░░░│')
        lines[6].append('│░░░░░░░░░│')
        lines[7].append('│░░░░░░░░░│')
        lines[8].append('│░░░░░░░░░│')
        lines[9].append('│░░░░░░░░░│ Dealer Hand')
        lines[10].append('└─────────┘')
        for i in range(11):
            for x in range(len(lines[i])):
                print(lines[i][x], end='')
            print()
    elif len(hand) > 2:
        ascii_display(hand)


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def bets():
    pass


def card_value(card):
    """Returns the integer value of a single card."""
    rank = card[0]
    if rank in ranks[0:-4]:
        return int(rank)
    elif rank is 'Ace':
        return 11
    else:
        return 10


def hand_value(hand):
    """Returns the integer value of the hand"""
    score = sum(card_value(card) for card in hand)
    num_aces = len([_ for _ in hand if _[0] is 'Ace'])
    while num_aces > 0:
        if score > 21 and 'Ace' in ranks:
            score -= 10
            num_aces -= 1
        else:
            break
    return score


def split():
    pass


def bust_check(player_hand):
    if hand_value(player_hand) > 21:
        print(f'You bust with a count of {hand_value(player_hand)}\n')
        play_again()
    elif hand_value(player_hand) == 21:
        print('You have 21! Dealers turn\n')
        pass
    else:
        pass
    print()


def game_state_start(dealer_hand, player_hand):
    print('Dealer Hand: ')
    ascii_display_dealer(dealer_hand)
    print('Your Hand: ', end='')
    [print(f'{player_hand[i][0]} of {player_hand[i][1]}, ', end='') for i in range(len(player_hand)-1)]
    print(f'{player_hand[len(player_hand)-1][0]} of {player_hand[len(player_hand)-1][1]}')
    ascii_display(player_hand)
    print(f'Your Count: {hand_value(player_hand)}\n')


def game_state(dealer_hand, player_hand):
    print('Dealer Hand: ', end='')
    [print(f'{dealer_hand[i][0]} of {dealer_hand[i][1]}, ', end='') for i in range(len(dealer_hand)-1)]
    print(f'{dealer_hand[len(dealer_hand)-1][0]} of {dealer_hand[len(dealer_hand)-1][1]}')
    ascii_display(dealer_hand)
    print('Your Hand: ', end='')
    [print(f'{player_hand[i][0]} of {player_hand[i][1]}, ', end='') for i in range(len(player_hand)-1)]
    print(f'{player_hand[len(player_hand)-1][0]} of {player_hand[len(player_hand)-1][1]}')
    ascii_display(player_hand)
    print(f'Your Count: {hand_value(player_hand)}')
    print(f'Dealer Count: {hand_value(dealer_hand)}\n')


def blackjack(hand):
    for m in range(len(hand)):
        if hand[m][0] == 'Ace':
            for n in range(len(hand)):
                if hand[n][0] == 'King' or hand[n][0] == 'Queen' or hand[n][0] == 'Jack':
                    return True


def play_again():
    x = input('Do you want to play again? (Yes = 1, No = 0) ')
    print()
    if x.lower()[0] == '1':
        game()
    elif x.lower()[0] == '0':
        clear()
        exit()


def game():
    clear()
    # add the betting functionality here
    # burn card
    deck.pop()
    # issue the player and dealer their first two cards
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    game_state_start(dealer_hand, player_hand)
    # add insurance if ace is shown
    if blackjack(dealer_hand):
        print('Dealer has blackjack\n')
        play_again()
    elif blackjack(player_hand):
        print('You have blackjack\n')
        play_again()
    # Players turn
    response = int(input('Hit or Stand? (Hit = 1, Stand = 0) '))
    # add split and double down
    print()
    while response:
        clear()
        hit(player_hand)
        game_state_start(dealer_hand, player_hand)
        bust_check(player_hand)
        response = int(input('Hit or Stand? (Hit = 1, Stand = 0) '))
    # dealers turn
    clear()
    game_state(dealer_hand, player_hand)
    # sort this logic out omg this is bad
    # check if dealer wins with current hand
    if hand_value(dealer_hand) > hand_value(player_hand):
        print(f'You Lose! Dealer has {hand_value(dealer_hand)} and you only have {hand_value(player_hand)}\n')
        play_again()
    elif hand_value(dealer_hand) == hand_value(player_hand):
        print(f'Push! You and the dealer both have {hand_value(dealer_hand)}\n')
        play_again()
    else:
        
        # dealer sticks once he gets to 17
        while hand_value(dealer_hand) < 17:
            time.sleep(3)
            hit(dealer_hand)
            clear()
            game_state(dealer_hand, player_hand)
            # check if bust
            if hand_value(dealer_hand) > 21:
                print(f'Dealer bust with count of {hand_value(dealer_hand)}, You win!\n')
                play_again()
        # check who won
        if hand_value(dealer_hand) > hand_value(player_hand):
            print(f'You Lose! Dealer has {hand_value(dealer_hand)} and you only have {hand_value(player_hand)}\n')
            play_again()
        elif hand_value(dealer_hand) == hand_value(player_hand):
            print(f'Push! You and the dealer both have {hand_value(dealer_hand)}\n')
            play_again()
        elif hand_value(dealer_hand) < hand_value(player_hand):
            print(f'You Win! Dealer has {hand_value(dealer_hand)} and you have {hand_value(player_hand)}\n')
            play_again()

if __name__ == '__main__':
    game()
