from pynput import keyboard
from pynput.keyboard import Listener
import time

PREV_DIRECTION = 'R'
SNAKE = [] # snake is a list of tuples. starts with 5 tuples and grows as the snake eats the food.
DIRECTION = "R" # direction in which the snake is moving. R-ight, L-eft, U-p or D-own.
#CURRENT_FOOD = None
BOARD = []

''' function to initialize the board'''
def initialize_board():
    global BOARD
    BOARD = [[0 for i in range(20)] for j in range(10)]

''' function to initialize the snake'''
def initialize_snake(board):
    SNAKE_HEAD =
    SNAKE = [[5, 4], [5, 3], [5, 2],[5, 1], [5,0]]
    for i in SNAKE:
        board[i[0]][i[1]] = 1

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
    PREV_DIRECTON = DIRECTION
    DIRECTION = key_direction[key]

''' function to randomly generate the food of the snake'''
def generate_food(snake, current_food):
    food_y = random.randint(0, 10)
    food_x = random.randint(0, 20)
    print(food_y, food_x)
    while snake[food_y][food_x] == 1:
        food_y = random.randint(0, 10)
        food_x = random.randint(0, 20)
        print(food_y, food_x)
    snake[food_y][food_x] = 2
    current_food = snake[food_y][food_x]

''' function to update the snake's position'''
def update_snake():
    global DIRECTION
    global PREV_DIRECTION
    global SNAKE
    if DIRECTION == 'L' and (PREV_DIRECTION == 'U' or PREV_DIRECTION == 'D'):
        print("turn to direction")
    elif DIRECTION == 'L' and (PREV_DIRECTION == 'L' or PREV_DIRECTION == 'R'):
        print("keep going at PREV_DIRECTION")
    elif DIRECTION == 'R' and (PREV_DIRECTION == 'U' or PREV_DIRECTION == 'D'):
        SNAKE.append([SNAKE[-1][0], SNAKE[-1][1]+1])
    elif DIRECTION == 'R' and (PREV_DIRECTION == 'L' or PREV_DIRECTION == 'R'):
        print("keep going at PREV_DIRECTION")
    elif DIRECTION == 'U' and (PREV_DIRECTION == 'L' or PREV_DIRECTION == 'R'):
        print("turn to DIRECTION")
    elif DIRECTION == 'U' and (PREV_DIRECTION == 'U' or PREV_DIRECTION == 'D'):
        print("keep going at PREV_DIRECTION")
    elif DIRECTION == 'D' and (PREV_DIRECTION == 'L' or PREV_DIRECTION == 'R'):
        print("turn to DIRECTION")
    elif DIRECTION == 'D' and (PREV_DIRECTION == 'U' or PREV_DIRECTION == 'D'):
        print("keep going at PREV_DIRECTION")
    else:
        print("else")

def game_step():
    global DIRECTION
    global PREV_DIRECTION
    stop_time = time.time() + 15
    while time.time() < stop_time:
        update_snake()
        time.sleep(1)

def play(board,snake, current_food, direction):
    pass

def main():
    BOARD = initialize_board()
    initialize_snake()
    generate_food()
    with Listener(on_press=change_direction) as l:
        game_step()
        l.join()
main()

