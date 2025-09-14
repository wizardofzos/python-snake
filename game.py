import curses
import time
import sys
from random import randint
from classes import Field
from classes import Snake


def main(screen):
    # Configure screen
    screen.timeout(0)

    # Init snake & field
    field = Field(10)
    snake = Snake("Joe")
    snake.set_field(field)
    speed = 0.4

    while(True):
        # Get last pressed key
        ch = screen.getch()
        if ch != -1:
            # If some arrows did pressed - change direction
            snake.set_direction(ch)

        # Move snake
        hit = snake.move()
        if hit == 1:
            # we ate a food
            if randint(1,10) > 6:
                # incrase speed every now and then...
                speed -= 0.05
        
        # Render field
        field.render(screen)
        screen.refresh()
        
        time.sleep(speed)

if __name__=='__main__':
    curses.wrapper(main)
