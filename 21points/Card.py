class Card():

    def __init__(self, variety, score, value):
        # 花色
        self.variety = variety
        # 点数
        self.score = score
        # 值
        self.value = value
        # 是否翻面
        self.bright = False

    def __str__(self, is_show_bright_card):
        if is_show_bright_card:
            return f"{self.variety}_{self.score}_{self.value}"
        else:
            if self.bright:
                return f"{self.variety}_{self.score}_{self.value}"
            else:
                return f"暗牌"

    # 明牌
    def set_is_bright(self, is_bright):
        self.bright = is_bright
        return self


