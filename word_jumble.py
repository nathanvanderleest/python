
# Word Jumble
#
# The computer picks a random word and then jumbles it
# The player has to guess the original word

import random

# create a sequence of words in a tuple
WORDS = ("python","jumble","easy","difficult","answer","xylophone")

# pick a word randomly
word = random.choice(WORDS)

# holds the correct word
correct = word

# create a jumbled word
jumbled = ""
while word:
    position = random.randrange(len(word))
    jumbled += word[position]
    word = word[:position] + word[(position+1):]

# Ready to start the game

print(
    """

        Welcome to the Word Jumble Game!

    Unscramble the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """)

print("The jumble is:",jumbled)

guess = input("Your guess: ")

while guess != correct and guess != "":
    guess = input("Thats incorrect, guess again: ")
    
if guess == "":
    print("Good, Bye")
else:
    print(guess,"is the correct answer!")






