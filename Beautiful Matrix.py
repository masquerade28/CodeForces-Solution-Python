                                                                        ''' MAIN LOGIC '''

                                            ''' To Be A Magic Matrix 1 Has To Be In The Center Of The Matrix, 
                                                        So To Count The Moves To Make It A Magic 
                We Will Subtract The Initial Position (x,y) Of 1 From The Desired Position (2,2) Of 1 [Starting Counting From (0,0)] '''

# We will create Nested Lists to create an Matrix
matrix = []

# Loop will run 5 times
# Will take 5 input in one run separated by space 
# And will append it to the main list matrix.

for i in range(5):
    matrix.append([int(i) for i in input().split()])

# initializing x and y for counting
(x,y) = (0,0)

# y = rows and x = columns
# Here we will find position of 1 and pull out it's index
for i in range(5):
    if matrix[i].count(1) > 0:
        y,x = (i, matrix[i].index(1))

# Counting moves 
print(abs(2-y)+ abs(2-x))
