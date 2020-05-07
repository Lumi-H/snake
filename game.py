# This file contains the game logic

SNAKE = [] # snake is a list of tuples. starts with 5 tuples and grows as the snake eats the food.
DIRECTION = "R" # direction in which the snake is moving. R-ight, L-eft, U-p or D-own.

# function to initialize the board
def initialize_board():
    board = [[i for i in range(20)] for j in range(10)]

def initialize_snake():
    SNAKE = []

def generate_food(snake):


def main():
    initialize_board()
    initialize_snake()

main()
