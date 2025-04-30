"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def up():
    """
    上
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def lock():
    """
    接上和下的動作
    """
    if not on_beeper():
        put_beeper()
    turn_right()
    move()
    turn_right()


def down():
    """
    下
    """
    while front_is_clear():
        move()
    turn_left()


def cross():
    """
    到另一個柱子
    """
    move()
    move()
    move()


def main():
    while front_is_clear():
        up()
        lock()
        down()
        cross()
    up()
    turn_left()
    turn_left()
    down()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)