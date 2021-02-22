import time
print("NUMBER GUESSING")
time.sleep(3)
print("I will think of a number. You have to guess it.")
time.sleep(3)
x = 0
n = int(input("Enter your number limit: "))
import random
r = random.randint(1, n)
while True:
	try:
		s = int(input("Enter your guess: "))
		break
	except ValueError:
		print("Please input a number.")
while s != r:
	if r > s:
		s = int(input("Enter a higher guess: "))
		x = x + 1
	if r < s:
		s = int(input("Enter a lower guess: "))
		x = x + 1
print(f"Congratulations! You guessed it in {x} tries!")