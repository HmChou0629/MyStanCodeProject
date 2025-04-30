"""
File: guess_my_number.py
Name:
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET = 32


def main():
    print("猜0-99")
    guess = int(input("請猜:"))
    while guess != SECRET:
        if guess > 99:
            print("你來亂的")
        elif guess < 0:
            print("你來亂的")
        elif guess > SECRET:
            print("太高")
        else:
            print("太低")
        guess = int(input("請猜:"))
    print("恭喜! 答案:" + str(SECRET))
    # print("猜0-99")
    # while True:
    #     guess = int(input("請猜:"))
    #     if guess > SECRET:
    #         print("太高")
    #     elif guess < SECRET:
    #         print("太低")
    #     else:
    #         break
    # print("恭喜! 答案:" + str(SECRET))


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
