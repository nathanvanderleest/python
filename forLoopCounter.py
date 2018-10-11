
# for loops
# Demonstrates the range() function

print("Counting:")

for i in range(10):
    print(i,end=" ")

print("\n\nCounting by fives:")
# start = 0, end at 50, count by 5
for i in range(0, 50, 5):
    print(i,end=" ")

print("\n\nCounting backwards:")
for i in range(10, 0, -1):
    print(i,end=" ")
