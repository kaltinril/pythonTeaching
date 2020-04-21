import random

# create the 10 x 10 array with random 0's and 1's
rows, cols = (10, 10) 
arr = [[random.randint(0, 1) for i in range(cols)] for j in range(rows)]

# Print out the array
print("\n Show starting array")
for i in range(len(arr)):
    print(arr[i])

# Add 5 to every odd column, in every even row
start_row = 0       # Start on 0, which I'm considering "even"
end_row = len(arr)  # for loop range is NOT inclusive of the endpoint
step_size = 2       # This allows us to skip the odd numbers by adding 2 to row each time
for row in range(start_row, end_row, step_size):
    # Start with ODD column (1), to size of row, go up by 2, staying on odds
    for col in range(1, len(arr[row]), 2):
        arr[row][col] += 5

# Print a blank line
print("\n Add 5 to every odd column, in every even row")

# Print out the final array
for i in range(len(arr)):
    print(arr[i])
