from game import Game
from deck import Deck
from hand import Hand
from money import Money
import sys


print("Welcome to the BlackJack Game!")
money = Money(5000)
while True:
    # Check if player has run out of money
    if money.amount <= 0:
        print("It is good that you were not playing with the real money!")
        print("Thanks for playing!")
        sys.exit()
    # Ask player to enter bet amount
    print("Money: ", money)
    bet = money.get_bet(money.amount)
    # Get dec
    deck = Deck()
    deck.shuffle()
    # give the dealer and player two cards from the deck
    player_hand = Hand()
    dealer_hand = Hand(dealer=True)
    for i in range(0,2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    # Handle player action
    print("Bet: ", bet)
    while True:
        dealer_hand.display()
        player_hand.display()
        # check if player has bust
        if player_hand.get_value() > 21:
            break
        # Get player's move
        game = Game()
        move = game.get_move(player_hand.get_value(), money.amount - bet)
        # Handle player move
        if move == 'D':
            additional_bet = money.get_bet(min(bet,(money.amount - bet)))
            bet += additional_bet
            print(f"Bet increased to {bet}")
            print(f"Bet: ", bet)
        if move in ('H', 'D'):
            # get another card
            new_card = deck.deal()
            rank = new_card.get_rank()
            suit = new_card.get_suit()
            print(f'You drew a {rank} of {suit}.')
            player_hand.add_card(new_card)
            if player_hand.get_value() > 21:
                continue
        if move == 'S':
            break
    # Handle dealer's action
    if player_hand.get_value() <= 21:
        while dealer_hand.get_value() < 12:
            print("The dealer hits..")
            dealer_hand.add_card(deck.deal())
            dealer_hand.display()
            player_hand.display()
            if dealer_hand.get_value() > 21:
                break
            input("Press enter to continue...")
            print('\n\n')
    # Handle whether the player won, lost or draw
    dealer_hand.display(show_dealer=True)
    player_hand.display()
    player_value = player_hand.get_value()
    dealer_value = dealer_hand.get_value()
    if dealer_value > 21:
        print(f"Dealer busts! You won ${bet}!")
        money.add_money(bet)
    elif player_value > 21:
        print(f"You lost")
        money.sub_money(bet)
    elif player_value > dealer_value:
        print(f"You win ${bet}!")
        money.add_money(bet)
    elif player_value == dealer_value:
        print(f'It is a draw and the bet is returned to you!')
        input("Press enter to continue...")
        print('\n\n')




















