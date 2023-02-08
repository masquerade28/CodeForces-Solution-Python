
                                                            ''' MAIN LOGIC '''

                                              ''' If algebric sum of all the forces is zero,
                                                          It is in equilibrium'''

# Taking Input For Number Of Forces Which Are Acting Upon The Object
forces = int(input())

# Creating an empty list to store the forces
L = []

# Appending the co-ordinates of the forces to the list L
for i in range(forces):
    L.append([int(i) for i in input().split()])

# Checking whether the sum of all the forces is zero or not
# If Yes, the object is in equilibrium
# Otherwise, it is not

if L[0][0] + L[1][0] + L[2][0] == 0 and L[0][1] + L[1][1] + L[2][1] == 0 and L[0][2] + L[1][2] + L[2][2] == 0 :
    print("YES")
else :
    print("NO")
