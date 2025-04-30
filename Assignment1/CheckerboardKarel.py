"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def fill_one_col():
    """
    走一行
    """
    while front_is_clear():
        put_beeper()
        move()
        if front_is_clear():
            move()


def turn_around():
    turn_left()
    turn_left()


def one_round():
    """
    上下一趟
    """
    turn_left()
    fill_one_col()
    check1()
    next_col1()
    check2()
    fill_one_col()
    check1()
    next_col2()


def next_col1():
    """
    上轉下
    """
    turn_right()
    move()


def next_col2():
    """
    下轉下一行
    """
    turn_left()
    if front_is_clear():
        move()


def check1():
    """
    上下檢查
    """
    turn_around()
    move()
    if on_beeper():
        turn_around()
        move()
    else:
        turn_around()
        move()
        put_beeper()


def check2():
    """
    左右檢查
    """
    turn_around()
    move()
    if on_beeper():
        turn_around()
        move()
        turn_right()
        move()
    else:
        turn_around()
        move()
        turn_right()


def main():
    while front_is_clear():
        one_round()
    if not front_is_clear():
        check1()
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
