class Player():

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.card_list = []

    def __str__(self, is_show_bright_card):
        str = ""
        for card in self.card_list:
            str += (card.__str__(is_show_bright_card) + ', ')
        return str[:-2]

    def get_score(self):
        return self.score

    def set_score(self, score=1):
        self.score += 1

    def reception_card(self, card):
        self.card_list.append(card)

    # 计算得分
    def calculate_value(self, is_calculate_bright_card):
        value = 0
        index = 0
        if is_calculate_bright_card:
            index = 0
        else:
            index = 1
        for card in self.card_list[index:]:
            if card.score != 'A':
                value += card.value
            else:
                if value <= 11:
                    value += 10
                else:
                    value += 1
        return value

    # 清空牌池
    def clear_card_list(self):
        self.card_list = []
