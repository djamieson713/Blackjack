import Cards

class Hand:
    def __init__(self):
        self.cards = []  # empty list
        self.value = 0
        self.aces = 0  # keep track of the number of aces

    def is_Ace(self, card):
        if (card.rank == 'Ace'):
            return True
        else:
            return False

    def add_cards(self, cards):
        for card in cards:
            self.cards.append(card)
            if self.is_Ace(card):
                self.aces = self.aces + 1

    def add_card(self, card):
        self.cards.append(card)
        if self.is_Ace(card):
            self.aces = self.aces + 1

    def compute_unadjusted_value(self):
        totalvalue = 0
        for card in self.cards:
            value = Cards.values[card.rank]
            totalvalue = totalvalue + value
        return totalvalue

    def subtract_for_ace(self, adjusted_value, no_of_aces):
        if (no_of_aces == 0):
            return adjusted_value

        if (adjusted_value < 22):
            return adjusted_value

        if (no_of_aces > 0) and (adjusted_value - 10) < 22:
            return adjusted_value - 10
        else:
            return self.subtract_for_ace(adjusted_value - 10, no_of_aces - 1)

    def adjust_for_ace(self):
        return self.subtract_for_ace(self.compute_unadjusted_value(), self.aces)

    def print_all_cards(self):
        for card in self.cards:
            print(card)

    def print_visible_cards(self):
        if len(self.cards) > 1:
            for card in self.cards[1:]:
                print(card)