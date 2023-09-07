from Player import Player
from Deck import Deck

if __name__ == '__main__':
    # 创建一副牌
    deck = Deck()
    deck.shuffle_list()
    # 创建一个玩家
    xlp = Player('xlp')
    AI = Player('AI')

    # 是否开始
    start_game = True
    # 初始化
    init_game = True
    # 游戏人数
    game_player_count = 2

    while start_game:
        print(f'----------游戏开始，剩余牌数：{len(deck)}----------')
        if len(deck) >= 4:
            print("发牌中......")
            if init_game:
                card = deck.distribute_card()
                xlp.reception_card(card)
                card = deck.distribute_card()
                AI.reception_card(card)

                card = deck.distribute_card()
                xlp.reception_card(card.set_is_bright(True))
                card = deck.distribute_card()
                AI.reception_card(card.set_is_bright(True))

                init_game = False
            else:
                pass
            print(f"xlp 的牌池：{xlp.__str__(False)}")
            print(f"AI 的牌池：{AI.__str__(False)}")
            print("------发牌结束-------")
            if len(deck) >= 1:
                distribute = input("是否需要发牌 1：是，0：否：")
                if distribute == '1':
                    card = deck.distribute_card()
                    xlp.reception_card(card.set_is_bright(True))
                    xlp_value = xlp.calculate_value(False)
                    if xlp_value >= 21:
                        print(f"xlp 的牌池：{xlp.__str__(True)}")
                        print(f"AI 的牌池：{AI.__str__(True)}")
                        print('AI 赢！')
                        AI.set_score()
                        xlp.clear_card_list()
                        AI.clear_card_list()
                        # 下一回合
                        init_game = True
                else:
                    print(f"xlp 的牌池：{xlp.__str__(True)}")
                    print(f"AI 的牌池：{AI.__str__(True)}")
                    xlp_value = xlp.calculate_value(True)
                    AI_value = AI.calculate_value(True)
                    if xlp_value > AI_value and xlp_value < 21:
                        print('xlp 赢！')
                        xlp.set_score()
                    elif xlp_value < AI_value or xlp_value > 21:
                        print('AI 赢！')
                        AI.set_score()
                    else:
                        print("平局！")
                    xlp.clear_card_list()
                    AI.clear_card_list()
                    # 下一回合
                    init_game = True
            else:
                start_game = False
        else:
            start_game = False

        print(f"xlp得分：{xlp.get_score()}, AI得分：{AI.get_score()}")


    print("游戏结束")