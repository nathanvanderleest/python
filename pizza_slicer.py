
# Pizza Slicer
# Demonstrates string slicing

word = "pizza"

print(
    """
    Slicing cheat sheet

    0   1   2   3   4   5
    +---+---+---+---+---+
    | P | i | z | z | a |
    +---+---+---+---+---+
   -5  -4  -3  -2  -1

    
    This doesn't make sense:
   -5  -4  -3  -2  -1   0   1   2   3   4   5
    +---+---+---+---+---+---+---+---+---+---+
    | p | i | z | z | a | p | i | z | z | a |
    -----------------------------------------
   
    """
)

print("Enter begnning and ending index for your slice of 'pizza'.")
print("Press enter key at 'Begin' to exit.")

# word[0:4] = word[:4]
# word[0:5] = word[:]
# word[2:5] = word[2:]

start = None
while start != "":

    start = input("\nStart: ")
    
    if start:
        start = int(start)
        finish = int(input("Finish: "))
        
        print("word[",start,":",finish,"] is", end=" ")
        print(word[start:finish])

print("done")
