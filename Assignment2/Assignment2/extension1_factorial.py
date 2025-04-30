"""
File: extension1_factorial.py
Name: 
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""


def main():
	"""
	TODO:
	"""
	total = 1
	print("Welcome to stanCode factorial master!")
	while True:
		n = int(input("Give me a number, and I will list the answer of factorial: "))
		if n == -100:
			print("- - - - - - See ya!-------------")
			break
		else:
			for i in range(1, n+1):
				total = total * i
			print("Ans: " + str(total))
			total = 1
	n = int(input("Give me a number, and I will list the answer of factorial: "))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()