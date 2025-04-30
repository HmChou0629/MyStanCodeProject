"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
constant = -100


def main():
	print("\"Weather Master 4.0!\"")
	print("Under 16℃ is coldest day")
	temp = int(input("Next temperature: (or -100 to quit)? "))
	if temp == constant:
		print("No temperatures were entered.")
	else:
		total = temp
		time = 1
		coldest_day = 0
		lowest_temperature = temp
		highest_temperature = temp
		while True:
			if temp == constant:
				break
			else:
				total = total + temp
				time += 1
				if temp < 16:
					coldest_day += 1
				if lowest_temperature > temp:
					lowest_temperature = temp
				if highest_temperature < temp:
					highest_temperature = temp
				temp = int(input("Next temperature: (or -100 to quit)? "))
		print("Highest temperature = " + str(highest_temperature))
		print("Lowest temperature = " + str(lowest_temperature))
		print("Average = " + str(total / time-1))
		print(str(coldest_day) + "cold day(s)")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
	main()
