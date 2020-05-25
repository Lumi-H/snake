from pynput import keyboard
from pynput.keyboard import Listener
import time
import random

PREV_DIRECTION = 'R'
SNAKE = [] # snake is a list of tuples. starts with 5 tuples and grows as the snake eats the food.
DIRECTION = "R" # direction in which the snake is moving. R-ight, L-eft, U-p or D-own.
#CURRENT_FOOD = None
BOARD = []
BOARD_DIMENSIONS = [10, 30]

''' function to initialize the board'''
def initialize_board():
    global BOARD
    BOARD = [[0 for i in range(BOARD_DIMENSIONS[1])] for j in range(BOARD_DIMENSIONS[0])]

''' function to initialize the snake'''
def initialize_snake():
    global SNAKE
    global BOARD
    SNAKE = [[4, 1], [4, 2], [4,3]]
    for i in SNAKE:
        BOARD[i[0]][i[1]] = 1

''' function to update the directon based on keyboard input'''
def update_direction(key):
    global DIRECTION
    global PREV_DIRECTION
    key_direction = {
    keyboard.Key.left: 'L',
    keyboard.Key.right: 'R',
    keyboard.Key.up: 'U',
    keyboard.Key.down: 'D'
    }

    PREV_DIRECTION = DIRECTION
    if key_direction[key] == 'L' and DIRECTION == 'R':
        DIRECTION = 'R'
    elif key_direction[key] == 'R' and DIRECTION == 'L':
        DIRECTION = 'L'
    elif key_direction[key] == 'D' and DIRECTION == 'U':
        DIRECTION = 'U'
    elif key_direction[key] == 'U' and DIRECTION == 'D':
            DIRECTION = 'D'
    else:
        DIRECTION = key_direction[key]
    print(DIRECTION)

''' function to randomly generate the food of the snake'''
def generate_food():
    food_y = random.randint(0, BOARD_DIMENSIONS[0]-1)
    food_x = random.randint(0, BOARD_DIMENSIONS[1]-1)
    print(food_y, food_x)
    while BOARD[food_y][food_x] == 1:
        food_y = random.randint(0, BOARD_DIMENSIONS[0]-1)
        food_x = random.randint(0, BOARD_DIMENSIONS[1]-1)
        print(food_y, food_x)
    BOARD[food_y][food_x] = 2

''' function to update the snake's position'''
def update_snake():
    global DIRECTION
    global PREV_DIRECTION
    global SNAKE
    global BOARD
    BOARD[SNAKE[0][0]][SNAKE[0][1]] = 0
    if (DIRECTION == 'L' and (PREV_DIRECTION == 'U' or PREV_DIRECTION == 'L'or PREV_DIRECTION == 'D')) or (DIRECTION == 'R' and PREV_DIRECTION == 'L'):
        if SNAKE[-1][1] != 0 and BOARD[SNAKE[-1][0]][SNAKE[-1][1]-1] != 1:
            if BOARD[SNAKE[-1][0]][SNAKE[-1][1]-1] != 2:
                SNAKE.pop(0)
                BOARD[SNAKE[0][0]][SNAKE[0][1]] = 0
            else:
                generate_food()
            BOARD[SNAKE[-1][0]][SNAKE[-1][1]-1] = 1
            SNAKE.append([SNAKE[-1][0],SNAKE[-1][1]-1])

            print("------------------------------------------------------")
            print(SNAKE)
            print(BOARD)
            print(PREV_DIRECTION)
            print(DIRECTION)
            print("------------------------------------------------------")
        else:
            print("hit the wall or ate itself")


    elif (DIRECTION == 'R' and (PREV_DIRECTION == 'U' or PREV_DIRECTION == 'D' or PREV_DIRECTION == 'R')) or (DIRECTION == 'L' and PREV_DIRECTION == 'R'):
        if SNAKE[-1][1] != len(BOARD[0])-1 and BOARD[SNAKE[-1][0]][SNAKE[-1][1]+1] != 1:
            if BOARD[SNAKE[-1][0]][SNAKE[-1][1]+1] != 2:
                SNAKE.pop(0)
                BOARD[SNAKE[0][0]][SNAKE[0][1]] = 0
            else:
                generate_food()
            BOARD[SNAKE[-1][0]][SNAKE[-1][1]+1] = 1
            SNAKE.append([SNAKE[-1][0],SNAKE[-1][1]+1])
            print("------------------------------------------------------")
            #print("snake[0][0] " + str(SNAKE[0][0]))
            #print("snake[0][1] " + str(SNAKE[0][1]))
            print(SNAKE)
            print(BOARD)
            print(PREV_DIRECTION)
            print(DIRECTION)
            print("------------------------------------------------------")
        else:
            print("hit the wall or ate itself")


    elif (DIRECTION == 'D' and (PREV_DIRECTION == 'R' or PREV_DIRECTION == 'D'or PREV_DIRECTION == 'L')) or (DIRECTION == 'U' and PREV_DIRECTION == 'D'):
        if SNAKE[-1][0] != len(BOARD)-1 and BOARD[SNAKE[-1][0]+1][SNAKE[-1][1]] != 1:
            if BOARD[SNAKE[-1][0]+1][SNAKE[-1][1]] != 2:
                SNAKE.pop(0)
                BOARD[SNAKE[0][0]][SNAKE[0][1]] = 0
            else:
                generate_food()
            BOARD[SNAKE[-1][0]+1][SNAKE[-1][1]] = 1
            SNAKE.append([SNAKE[-1][0]+1,SNAKE[-1][1]])
            print("------------------------------------------------------")
            print(SNAKE)
            print(BOARD)
            print(PREV_DIRECTION)
            print(DIRECTION)
            print("------------------------------------------------------")
        else:
            print("hit the wall or ate itself")

    elif (DIRECTION == 'U' and (PREV_DIRECTION == 'R' or PREV_DIRECTION == 'L' or PREV_DIRECTION == 'U')) or (DIRECTION == 'D' and PREV_DIRECTION == 'U'):
        if SNAKE[-1][0] != 0 and BOARD[SNAKE[-1][0]-1][SNAKE[-1][1]] != 1:
            if BOARD[SNAKE[-1][0]-1][SNAKE[-1][1]] != 2:
                SNAKE.pop(0)
                BOARD[SNAKE[0][0]][SNAKE[0][1]] = 0
            else:
                generate_food()
            BOARD[SNAKE[-1][0]-1][SNAKE[-1][1]] = 1
            SNAKE.append([SNAKE[-1][0]-1,SNAKE[-1][1]])
            print("------------------------------------------------------")
            print(SNAKE)
            print(BOARD)
            print(PREV_DIRECTION)
            print(DIRECTION)
            print("------------------------------------------------------")
        else:
            print("hit the wall or ate itself")

    else:
        print('else statement reached')


def game_step():
    global DIRECTION
    global PREV_DIRECTION
    stop_time = time.time() + 120
    while time.time() < stop_time:
        update_snake()
        time.sleep(1)

def play():
    pass

def main():
    BOARD = initialize_board()
    initialize_snake()
    generate_food()
    with Listener(on_press=update_direction) as l:
        game_step()
        l.join()
main()
