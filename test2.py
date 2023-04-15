amount = 0
board = [[0] * 100 for _ in range(100)]  # 初始化棋盘

def cover(tr, tc, dr, dc, size):
    """
    用三格板覆盖棋盘
    """
    global amount, board
    if size < 2:
        return

    amount += 1
    t = amount
    s = size // 2

    if dr < tr + s and dc < tc + s:  # 残缺棋盘位于左上
        cover(tr, tc, dr, dc, s)
        board[tr + s - 1][tc + s] = t
        board[tr + s][tc + s - 1] = t
        board[tr + s][tc + s] = t
        cover(tr, tc + s, tr + s - 1, tc + s, s)
        cover(tr + s, tc, tr + s, tc + s - 1, s)
        cover(tr + s, tc + s, tr + s, tc + s, s)
    elif dr < tr + s and dc >= tc + s:  # 残缺方格位于右上
        cover(tr, tc + s, dr, dc, s)
        board[tr + s - 1][tc + s - 1] = t
        board[tr + s][tc + s - 1] = t
        board[tr + s][tc + s] = t
        cover(tr, tc, tr + s - 1, tc + s - 1, s)
        cover(tr + s, tc, tr + s, tc + s - 1, s)
        cover(tr + s, tc + s, tr + s, tc + s, s)
    elif dr >= tr + s and dc < tc + s:  # 残缺方格位于左下
        cover(tr + s, tc, dr, dc, s)
        board[tr + s - 1][tc + s - 1] = t
        board[tr + s - 1][tc + s] = t
        board[tr + s][tc + s] = t
        cover(tr, tc, tr + s - 1, tc + s - 1, s)
        cover(tr, tc + s, tr + s - 1, tc + s, s)
        cover(tr + s, tc + s, tr + s, tc + s, s)
    else:  # 残缺方格位于右下
        cover(tr + s, tc + s, dr, dc, s)
        board[tr + s - 1][tc + s - 1] = t
        board[tr + s - 1][tc + s] = t
        board[tr + s][tc + s - 1] = t
        cover(tr, tc, tr + s - 1, tc + s - 1, s)
        cover(tr, tc + s, tr + s - 1, tc + s, s)
        cover(tr + s, tc, tr + s, tc + s - 1, s)

def output_board(size):
    """
    输出棋盘
    """
    for i in range(size):
        for j in range(size):
            print(board[i][j], end='\t')
        print()

k = int(input("输入K的值："))
size = 1
for i in range(k):
    size *= 2

x, y = map(int, input("输入残缺棋盘中残缺的位置：").split())
board = [[0]*size for _ in range(size)]
cover(0, 0, x, y, size)
output_board(size)
