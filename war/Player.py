
class Player():
    war_pool = []
    play_poker = None
    def __init__(self, name, deck):
        self.name = name
        # 牌组，最多26张
        self.deck = deck

    # 出牌
    def play(self):
        if len(self.deck) > 0:
            self.play_poker = self.deck.pop()
            return self.play_poker
        else:
            return None
    # 回收牌
    def recycle_poker(self, poker):
        self.deck.insert(0, poker)

    # 赢牌之后加牌
    def win(self, poker, war_pool):
        self.deck.insert(0, self.play_poker)
        self.deck.insert(0, poker)
        for i in range(0, len(war_pool)):
            self.deck.insert(0, war_pool.pop())

    # 丢弃最上面三张，丢入战争池
    def choose_poker_to_war_pool(self):
        if len(self.deck) <= 3 and len(self.deck) > 1:
            for i in range(1, len(self.deck)):
                self.war_pool.append(self.deck.pop())
        elif len(self.deck) > 3:
            for i in range(0, 3):
                self.war_pool.append(self.deck.pop())
        else:
            pass
