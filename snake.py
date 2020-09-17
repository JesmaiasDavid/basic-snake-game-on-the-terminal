import curses
from random import randint

# set up the window
curses.initscr()  # initializing
y = 20
x = 80
window = curses.newwin(y, x, 0, 0)  # creates the window
window.keypad(True)  # to accept keyboard input
curses.noecho()
curses.curs_set(0)
window.border()  # adds a border to the window
window.nodelay(True)

# snake and food
snake = [(6, 10), (6, 9), (6, 8)]
food = (13, 28)

window.addch(food[0], food[1], "#")  # add the food at the beginning of the game

score = 0

ESC = 27  # Escape key
key = curses.KEY_RIGHT  # right arrow key

# logic of the game
while key != ESC:

    window.addstr(0, 2, 'Score : %s ' % score)  # adds the score in the window
    window.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120)  # increases the speed based on the length of the snake

    prev_key = key
    event = window.getch()  # waits for the user to hit a key
    key = event if event != -1 else prev_key

    if key not in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

    # get the value of x and y from the head of the snake
    y = snake[0][0]
    x = snake[0][1]

    # calculate the next coordinates of the snake
    if key == curses.KEY_DOWN:
        y += 1
    if key == curses.KEY_UP:
        y -= 1

    if key == curses.KEY_LEFT:
        x -= 1
    if key == curses.KEY_RIGHT:
        x += 1

    snake.insert(0, (y, x))

    # check if the snake hit the boarder
    if y == 0:
        break
    if y == 19:
        break
    if x == 0:
        break
    if y == 79:
        break

    # check if snakes runs over itself
    if snake[0] in snake[1:]:
        break

    if snake[0] == food:
        # snake eat the food
        score += 1
        food=()

        while food == ():
            food = (randint(1, 18), randint(1, 78))
            if food in snake:
                food = ()

        window.addch(food[0], food[1], '#')

    else:  # move snake
        last = snake.pop()
        window.addch(last[0], last[1], ' ')

    window.addch(snake[0][0], snake[0][1], '*')

print("Final score : %s" % score)
