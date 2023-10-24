import p1_random


def card_num(n, rng):  # card generator
    card = rng.next_int(n) + 1
    if card == 1:
        print("Your card is a ACE!")
    if 1 < card < 11:
        print("Your card is a " + str(card) + "!")
    if card == 11:
        print("Your card is a JACK!")
        card = 10
    if card == 12:
        print("Your card is a QUEEN!")
        card = 10
    if card == 13:
        print("Your card is a KING!")
        card = 10
    return card


def main():
    rng = p1_random.P1Random()

    hand = 0  # starting values
    run = 0
    win = 0
    loss = 0
    tie = 0

    game = False
    while run >= 0:
        hand = 0
        print(f"START GAME #{run + 1}\n")  # prints out starting hand
        card = card_num(13, rng)
        hand += card
        print(f"Your hand is: {card}\n")
        game = True

        while game and run >= 0:
            menu = int(input(f'1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n'))
            print("Choose an option:")
            if menu == 4:
                run = -1000  # breaks out of the game when the player inputs 4
                break

            if menu == 1:  # checks for win/loss conditions
                hand += card_num(13, rng)
                print(f"Your hand is: {hand}\n")

                if hand > 21:
                    print("You exceeded 21! You lose.")
                    loss += 1
                    break
                if hand == 21:
                    print("BLACKJACK! You win!")
                    win += 1
                    break
                else:
                    continue

            if menu == 2:
                dealer = rng.next_int(11) + 16  # generates dealer hand
                print("Dealer's hand: " + str(dealer))
                print(f"Your hand is: {hand}")

                if dealer == hand:
                    print("It's a tie! No one wins!")
                    tie += 1
                    break

                if 21 >= dealer > hand:
                    print("Dealer wins!")
                    loss += 1
                    break

                if dealer < hand:
                    print(f"BLACKJACK! You win!\n")
                    win += 1
                    break

                else:
                    print(f"You win!\n")
                    win += 1
                    break

            if menu == 3:  # game statistics
                print(f"Number of Player wins: {win}")
                print(f"Number of Dealer wins: {loss}")
                print(f'Number of tie games: {tie}')
                print(f'Total # of games played is: {run}')
                if run != 0:
                    print(f"Percentage of Player wins: {(win / run) * 100} %")

            else:
                print(f"Invalid input!\nPlease enter an integer value between 1 and 4.")
        run += 1  # keeps track of games


if __name__ == '__main__':
    main()
