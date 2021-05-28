def solution(board):
    solve(board)
    return board


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, column = find
    for i in range(1, 10):
        if valid(bo, i, (row, column)):
            bo[row][column] = i
            if solve(bo):
                return True
            bo[row][column] = 0
    return False


def valid(bo, num, pos):
    for i in range(len(bo[pos[0]])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = (pos[0] // 3) * 3
    box_y = (pos[1] // 3) * 3
    for i in range(3):
        for j in range(3):
            if box_x + i == pos[0] and box_y + j == pos[1]:
                continue
            if bo[box_x + i][box_y + j] == num:
                return False
    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return i, j
    return False
