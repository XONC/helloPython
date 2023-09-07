from random import randint
class Deck():
    basePoker = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = []
    def __init__(self):
        for pokerIndex in range(0, len(self.basePoker)):
            self.deck.append((pokerIndex, self.basePoker[pokerIndex]))
            self.deck.append((pokerIndex, self.basePoker[pokerIndex]))
            self.deck.append((pokerIndex, self.basePoker[pokerIndex]))
            self.deck.append((pokerIndex, self.basePoker[pokerIndex]))
    def get_deck(self):
        return self.deck
    # 发牌
    def deal_card(self, *args):
        while len(self.deck) > 0:
            for arg in args:
                index = randint(0, len(self.deck) - 1)
                arg.append(self.deck.pop(index))
