from Deck import Deck
from Player import Player

if __name__ == '__main__':
    deck = Deck()
    xlp = Player(name='xlp', deck=[])
    wx = Player(name='wx', deck=[])
    deck.deal_card(xlp.deck, wx.deck)
    # print(xlp.deck)
    # print(wx.deck)
    while len(xlp.deck) != 52 and len(wx.deck) != 52:
        xlp_poker = xlp.play()
        wx_poker = wx.play()
        if xlp_poker != None and wx_poker != None:
            if xlp_poker[0] > wx_poker[0]:
                xlp.win(wx_poker, wx.war_pool)
            elif xlp_poker[0] < wx_poker[0]:
                wx.win(xlp_poker, xlp.war_pool)
            else:
                xlp.recycle_poker(xlp_poker)
                xlp.choose_poker_to_war_pool()

                wx.recycle_poker(wx_poker)
                wx.choose_poker_to_war_pool()


    print(len(xlp.deck))
    print(len(wx.deck))


