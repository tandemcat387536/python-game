"""
Autor : Matej Kovár

"""
from random import randint


# Generates empty plan
def empty_plan(n):
    return [[0 for _ in range(n)]
            for _ in range(n)]


# Prints plan
# free place -> '.'
# player_placed -> 'X'
# AI_placed -> 'O'
# blocks around player or AI -> '#'
def print_plan(plan, n):
    symbol = {0: ".", 1: "X", 2: "O", 3: "#"}
    for i in range(n):
        for j in range(n):
            print(symbol[plan[i][j]], end=" ")
        print()
    print()
    return


def game_over(plan, n):
    for i in range(n):
        for j in range(n):
            if plan[i][j] == 0:
                return False
    return True


def check_turn(plan, n, x, y):
    if 0 < x <= n and 0 < y <= n:
        if plan[y - 1][x - 1] == 0:
            return True
    return False


def make_turn(plan, n, x, y, player):
    for i in range(n):
        for j in range(n):
            if abs((y - 1) - i) <= 1 and abs((x - 1) - j) <= 1:
                plan[i][j] = 3
    plan[y - 1][x - 1] = player
    return plan


# AI strategy -> places in random positions
def strategy(plan, n):
    x = randint(1, n)
    y = randint(1, n)
    if check_turn(plan, n, x, y):
        return str(x) + " " + str(y)
    else:
        return strategy(plan, n)


def play(mode, rows):
    plan = empty_plan(rows)
    player = 1
    while game_over(plan, rows) is False:
        print_plan(plan, rows)
        if mode == 1:
            move = input("Player " + str(player) + " move x y: ")
        else:
            if player == 1:
                move = input("Player 1 move x y: ")
            else:
                move = strategy(plan, rows)
                print("AI move x y:", move)
        x, y = list(map(int, move.split(" ")))
        if check_turn(plan, rows, x, y):
            plan = make_turn(plan, rows, x, y, player)
            player = 3 - player
        else:
            print("Invalid move, try again")
            print()
    print_plan(plan, rows)
    player = 3 - player
    if mode == 2:
        if player == 2:
            player = "AI"
    print("Player " + str(player) + " wins.")
    return


play(2, 10)
# mode = 1  -> game 1 vs 1
# mode = 2  -> game 1 vs AI
