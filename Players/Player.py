

class Player:
    def __init__(self, identifier, total):
        self.total = total
        self.bet = 0
        self.hand = None
        self.identifier = identifier
        self.status = "play"

    def make_bet(self, amount):
        if (self.total - amount) < 0:
            print("This bet is more than you have in your account, please add money")
        else:
            self.bet = amount

    def initialHand(self, hand):
        self.hand = hand

    def win_bet(self):
        self.total = self.total + self.bet

    def lose_bet(self):
        self.total = self.total - self.bet

