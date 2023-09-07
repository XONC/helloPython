from random import shuffle
from Card import Card
class Deck():
    variety_list = ["黑桃", "红桃", "梅花", "方块"]
    score_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    score_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 10}
    king = "KING"
    joker = "JOKER"
    card_list = []

    def __init__(self):
        for score in self.score_list:
            for variety in self.variety_list:
                value = self.score_value[score]
                self.card_list.append(Card(variety, score, value))

    def __str__(self):
        str = ""
        for card in self.card_list:
            str += card.__str__()
        return str

    def __len__(self):
        return len(self.card_list)

    def shuffle_list(self):
        return shuffle(self.card_list)

    def distribute_card(self):
        return self.card_list.pop()


