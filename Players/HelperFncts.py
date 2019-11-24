def print_all_hands(dealer, players):
    print('========================================================')
    print(dealer.identifier + " Hand, Remember one card is hidden.")
    dealer.hand.print_visible_cards()
    print('========================================================')
    print("")
    for player in players:
        print('========================================================')
        print(player.identifier + " Hand")
        player.hand.print_all_cards()
        print('========================================================')
    print("")


def print_player_statuses(dealer, players):
    print('========================================================')
    print(dealer.identifier + " has status of " + dealer.status)
    if dealer.status != 'bust':
        print("The value of the dealer hand is: " + str(dealer.hand.adjust_for_ace()))
    print('========================================================')
    print(' ')
    for player in players:
        print('========================================================')
        print(player.identifier + " has status of " + player.status)
        print("The value of the player hand is: " + str(player.hand.adjust_for_ace()))
        print('========================================================')
    print(' ')

def determine_if_anyone_can_play(players):
    for player in players:
        if player.status == 'play':
            return True
    return False

def place_bets(players):
    for player in players:
        print('========================================================')
        print(player.identifier)
        inputString = input('Please enter your bet:')
        player.make_bet(int(inputString))
        print('========================================================')
        print(' ')