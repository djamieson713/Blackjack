from Cards import Deck, Hand
from Players import Player, print_all_hands, print_player_statuses, determine_if_anyone_can_play, place_bets

class Manager:
    def __init__(self, noplayers, initial_stake):
        self.players = []
        self.dealer = Player("Dealer", 10000)
        self.deck = Deck()
        self.deck.shuffle()
        cards = self.deck.deal(2)
        dealerHand = Hand()
        dealerHand.add_cards(cards)
        self.dealer.initialHand(dealerHand)

        for i in range(0, noplayers):
            player = Player("Player" + str(i + 1), initial_stake)
            cards = self.deck.deal(2)
            playerHand = Hand()
            playerHand.add_cards(cards)
            player.initialHand(playerHand)
            self.players.append(player)
        print_all_hands(self.dealer, self.players)
        self.play_rounds()

    def hit_or_hold(self):
        while determine_if_anyone_can_play(self.players):
            for player in self.players:
                if player.status == "play":
                    print("==============================================")
                    print(player.identifier)
                    inputString = input('Do you want to hit or hold?')
                    print("==============================================")
                    if inputString == "hold":
                        player.status = "hold"
                    elif inputString == "hit":
                        card = self.deck.deal(1)[0]
                        player.hand.add_card(card)
                        handvalue = player.hand.adjust_for_ace()
                        print("The value of the current hand is " + str(handvalue))
                        print("==============================================")
                        if handvalue > 21:
                            player.status = 'bust'

    def finish_dealer_hand(self):
        print("Here are the dealer's cards")
        for card in self.dealer.hand.cards:
            print(card)
        print("+==================================================")
        dealervalue = self.dealer.hand.adjust_for_ace()
        print("Initial hand value for dealer: " + str(dealervalue))
        while dealervalue < 17:
            card = self.deck.deal(1)[0]
            print(card)
            self.dealer.hand.add_card(card)
            dealervalue = self.dealer.hand.adjust_for_ace()
            print("The value of dealer hand with card added is: " + str(dealervalue))
            if dealervalue > 21:
                self.dealer.status = 'bust'

    def pay_bets(self):
        for player in self.players:
            if player.status == 'bust':
                player.lose_bet()
            elif self.dealer.status == 'bust':
                player.win_bet()
            elif player.hand.adjust_for_ace() > self.dealer.hand.adjust_for_ace():
                player.win_bet()
            else:
                player.lose_bet()
            print('==================================================================')
            print(player.identifier + " now has this total : " + str(player.total))

    def play_rounds(self):
        want_to_play_game = True
        while want_to_play_game:
           place_bets(self.players)
           self.hit_or_hold()
           self.finish_dealer_hand()
           print_player_statuses(self.dealer, self.players)
           self.pay_bets()
           print('==================================================================')
           inputString = input('Do you want to play again: yes/no?')
           if inputString == 'no':
               want_to_play_game = False
           else:
               cards = self.deck.deal(2)
               dealerHand = Hand()
               dealerHand.add_cards(cards)
               self.dealer.initialHand(dealerHand)
               for player in self.players:
                   cards = self.deck.deal(2)
                   playerHand = Hand()
                   playerHand.add_cards(cards)
                   player.initialHand(playerHand)
                   player.status = 'play'
           print('==================================================================')


manager = Manager(3, 1000)