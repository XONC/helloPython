def start():
    white_chess = '%'
    black_chess = '#'
    chessboard = [['0', '0', '0'], ['0', '0', '0'], ['0', '0', '0']]
    chess = black_chess
    while not winner(chess, chessboard):
        if chess == black_chess:
            chess = white_chess
        else:
            chess = black_chess
        chessboard = play_chess(chess, chessboard)
    else:
        print(f'{chess} 赢得了胜利！')
        display(chessboard)

# 下棋
def play_chess(chess, chessboard):
    display(chessboard)
    position1 = input(f'当前棋手：{chess},请下棋：')
    position = position1.replace(' ','').replace('，', ',').split(',')
    print(chessboard[int(position[0])][int(position[1])])
    if chessboard[int(position[0])][int(position[1])] == '0':
        chessboard[int(position[0])][int(position[1])] = chess
        return chessboard
    else:
        print('此位置已经有人了')
        return play_chess(chess, chessboard)
# 渲染棋盘
def display(chessboard):
    one_row = chessboard[0]
    two_row = chessboard[1]
    three_row = chessboard[2]
    print(one_row)
    print(two_row)
    print(three_row)
# 判断胜利条件
def winner(chess, chessboard):
    return win_method_1(chess, chessboard) or win_method_2(chess, chessboard) or win_method_3(chess, chessboard)
# 4种胜利条件
def win_method_1(chess, chessboard):
    for items in chessboard:
        if ''.join(items) == chess*3:
            return True
    return False
def win_method_2(chess,chessboard):
    one_row = chessboard[0]
    two_row = chessboard[1]
    three_row = chessboard[2]
    for i in range(0, 3):
        if (one_row[i] + two_row[i] + three_row[i]) == chess*3:
            return True
    return False
def win_method_3(chess,chessboard):
    one_row = chessboard[0]
    two_row = chessboard[1]
    three_row = chessboard[2]
    return (one_row[0] + two_row[1] + three_row[2]) == chess*3 or (one_row[2] + two_row[1] + three_row[0]) == chess*3

if __name__ == '__main__':
    start()