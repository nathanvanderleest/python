
# while loops
#use Ctrl+C to terminate the program.

import random

num1 = random.randint(1,6)

print("Guess the number:", end=" ")

guess = int(input())
count = 1
while guess != num1:
    guess = int(input("Guess again: "))
    count += 1

print("Your Right! It took you", count, "guesses")


