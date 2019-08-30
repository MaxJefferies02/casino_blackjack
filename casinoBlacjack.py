from random import shuffle
import os
import time

ranks = [_ for _ in range(2, 11)] +  ['Jack', 'Queen','King', 'Ace']
suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']


def get_deck():
    return [[rank,suit] for rank in ranks for suit in suits]

deck = get_deck()
shuffle(deck)


def reshuffle():
    deck = get_deck()
    shuffle(deck)


def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')


def card_value(card):

    rank = card[0]
    if rank in ranks [0:-4]:
        return int(rank)
    elif rank == 'Ace':
        return 11
    else:
        return 10


def bet_value():
    while True:
        try:
            total = int(input("How much money have you brought to the table? £"))
        except ValueError:
            print("Sorry must be an integer...")
        else:
            break
    while True:
        try:
            bet = int(input("How much are you going to bet? £"))
        except ValueError:
            print("Sorry must be an integer...")
        else:
            if bet > total:
                print(f"Sorry You only have {total}. Your bet must not exceed this.")
            elif bet == 0:
                print("Sorry, the minimum stake is £1")
                exit()
            else:
                print("Good Luck!")
                time.sleep(2)
                clear()
                break
    return bet
    return total

def hand_value(hand):
    score = sum(card_value(card) for card in hand)
    num_aces = len([_ for _ in hand if _[0] is 'Ace'])
    while num_aces > 0:
        if score > 21 and 'Ace' in ranks:
            score -= 10
            num_aces -= 1
        else:
            break
    return score


def bust(player_hand):
    if hand_value(player_hand) > 21:
        print("You went bust! You lose!")
        play_again()
    elif hand_value(player_hand) == 21:
        print('You have 21! Dealers turn')
        pass
    else:
        pass


def hit(hand):
    new_player_card = deck.pop()
    hand.append(new_player_card)


def play_again():
    replay = input("Do you want to play again? (enter Yes or No) ")
    print()
    if replay.lower()[0] == 'y':
        clear()
        print("reshuffling.")
        time.sleep(0.5)
        clear()
        print("reshuffling..")
        time.sleep(0.5)
        clear()
        print("reshuffling...")
        time.sleep(0.5)
        clear()
        print("reshuffling..")
        time.sleep(0.5)
        clear()
        print("reshuffling.")
        time.sleep(0.5)
        clear()
        print("reshuffling")
        time.sleep(0.5)
        clear()
        print("reshuffling.")
        time.sleep(0.5)
        clear()
        print("reshuffling..")
        time.sleep(0.5)
        clear()
        print("reshuffling...")
        time.sleep(0.5)
        clear()
        print("reshuffling..")
        time.sleep(0.5)
        clear()
        print("reshuffling.")
        time.sleep(0.5)
        clear()
        reshuffle()
        game()
    elif replay.lower()[0] =='o':
        clear()
        reshuffle()
        time.sleep(1)
        game()
    elif replay.lower()[0] == 'n':
        clear()
        exit()


def blackjack(hand):
    for m in range(len(hand)):
        if hand[m][0] == 'Ace':
            for n in range(len(hand)):
                if hand[n][0] == 'King' or hand [n][0] == 'Queen' or hand [n][0] =='Jack':
                    return True


def card_display(hand):
    lines = [[] for i in range(11)]
    for card in hand:
        if card[0] == 'Jack' or card[0] == 'King' or card[0] == 'Queen' or card[0] == 'Ace':
            label = card[0].rstrip('ackinguenc')
            space = ' '
        elif card[0] == 10:
            label = '10'
            space = ''
        else:
            label = card[0]
            space = ' '
        if card[1] == 'Spades':
            symbol = '♠'
        elif card[1] == 'Diamonds':
            symbol = '♦'
        elif card[1] == 'Hearts':
            symbol = '♥'
        else:
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
                print(lines[i][x], end=' ')
            else:
                print(lines[i][x], end='')
        print()


def card_display_dealer(hand):
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
        lines[9].append('│░░░░░░░░░│ ')
        lines[10].append('└─────────┘')
        for i in range(11):
            for x in range(len(lines[i])):
                print(lines[i][x], end='')
            print()
    elif len(hand) > 2:
        card_display(hand)


def game_state(dealer_hand, player_hand):
    card_display_dealer(dealer_hand)
    card_display(player_hand)
    print(f"Your count: {hand_value(player_hand)}")


def game():
    clear()
    print("Welcome to Blackjack!")
    deck.pop()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    while True:
        try:
            total = int(input("How much money have you brought to the table? £"))
        except ValueError:
            print("Sorry must be an integer...")
        else:
            break
    while True:
            try:
                bet = int(input("How much are you going to bet? £"))
            except ValueError:
                print("Sorry must be an integer...")
            else:
                if bet > total:
                    print(f"Sorry You only have {total}. Your bet must not exceed this.")
                elif bet == 0:
                    print("Sorry, the minimum stake is £1")
                    exit()
                else:
                    print("Good Luck!")
                    time.sleep(2)
                    clear()
                    break
    game_state(dealer_hand, player_hand)
    if blackjack(dealer_hand):
        print('Dealer has Blackjack! You Lose!')
        print(f'You lost £{bet}')
        play_again()
    elif blackjack(player_hand):
        print('You got Blackjack! You Win!')
        print(f'You won £{bet*2}')
        play_again()
    twist = int(input('Would you like to hit[1] or stand[0]? '))
    print()
    while twist:
        clear()
        hit(player_hand)
        game_state(dealer_hand, player_hand)
        bust(player_hand)
        five_check(player_hand)
        if len(player_hand) >= 5:
            print("5 card trick!")
            print(f'You win £{bet*2}')
            play_again()
        twist = int(input('Hit[1] or Stand[0]?'))

    clear()
    game_state(dealer_hand, player_hand)
    if hand_value(dealer_hand) > hand_value(player_hand):
        print(f"You Lose! Dealer is closer to 21 with a total of {hand_value(dealer_hand)}!")
        print(f'You lost £{bet}')
        play_again()
    elif hand_value(dealer_hand) == hand_value(player_hand):
        print(f"Push! You both have {hand_value(dealer_hand)}")
        play_again()
    else:
        while hand_value(dealer_hand) < 17:
            time.sleep(1)
            hit(dealer_hand)
            five_check(dealer_hand)
            if len(dealer_hand) >= 5:
                print("5 card trick!")
                print(f'You lose £{bet}')
                play_again()
            game_state(dealer_hand, player_hand)
            clear()
            game_state(dealer_hand, player_hand)

            if hand_value(dealer_hand) > 21:
                print("Dealer went bust! You Win!")
                print(f'You won £{bet*2}')
                play_again()

        if hand_value(dealer_hand) > hand_value(player_hand):
            print(f"You Lose! Dealer is closer to 21 with a total of {hand_value(dealer_hand)}")
            print(f'You lost £{bet}')
            play_again()
        elif hand_value(dealer_hand) == hand_value(player_hand):
            print(f"Push! You both have {hand_value(dealer_hand)}.")
            play_again()
        elif hand_value(player_hand) > hand_value(dealer_hand):
            print(f"You have {hand_value(player_hand)} and the Dealer has {hand_value(dealer_hand)}. You are closer to 21! You Win!")
            print(f'You won £{bet*2}')
            play_again()
        elif hand_value(dealer_hand) == 21:
            print("Dealer got 21! You Lose!")
            print(f'You lost £{bet}')
            play_again()


if __name__ == '__main__':
    game()
