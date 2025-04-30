"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO:
    """
    print("This program computes Hailstone sequences")
    x = int(input("Enter a number: "))
    times = 0
    while True:
        if x == 1:
            break
        if x % 2 == 0:
            print(str(int(x)) + " is even, so i take half: ")
            x = x / 2
            times += 1
        else:
            print(str(int(x)) + " is odd, so i make 3n+1: ")
            x = 3 * x + 1
            times += 1
    print("It took "+str(times)+" steps to reach 1")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
