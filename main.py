import time
print("NUMBER GUESSING")
time.sleep(3)
print("I will think of a number. You have to guess it.")
time.sleep(3)
x = 0
n = input("Enter your number limit: ")
while True:
	try:
		int(n)
		break
	except ValueError:
		n = input("Only enter an integer value: ")
n = int(n)
import random
r = random.randint(1,n)
while True:
	try:
		s = int(input("Enter your guess: "))
		break
	except ValueError:
		print("Please input an ineger: ")
while s != r:
	if r > s:
		while True:
			try:
				s = int(input("Enter a higher guess: "))
				break
			except ValueError:
				s = input("Only enter an integer value: ")
		x = x + 1
	if r < s:
		while True:
			try:
				s = int(input("Enter a lower guess: "))
				break
			except ValueError:
				s = input("Only enter an integer value: ")
		x = x + 1
print(f"Congratulations! You guessed it in {x} tries!")