
import random

# generate random numbers 1 - 6
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2

guess = int(input("Guess the number:"))

if guess > die1:
    print("Too high")
elif guess < die1:
    print("Too low")
else:
    print("I think your right.")

if guess != die1:
    print("Incorrect")

if guess == die1:
    print("Your Right!")
else:
    print("Incorrect")

print("you rolled:", die1, "and a", die2, "for a total of",total)

if die1:
    print(die1)
else:
    print("The dice is zero")

if "apple" < "orange":
    print("apple comes before orange in the dictionary")

#input()






