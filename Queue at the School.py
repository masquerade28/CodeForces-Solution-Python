# This takes two inputs separated by space and converts them into integer
n,t = map(int,input().split())

# This takes the string, if it is in lowercase-converts into uppercase and converts it into list for looping 
string = list(str(input()).upper())

j = 0

# Running loop t times
while j < t:
    
    i = 0
    
    # Looping through the list
    while i < len(string)-1:
        
        # Checking whether the Boy is standing infront of Girl
        if string[i] == "B" and string[i+1] == "G":
            
            # If Yes, Swap the positions
            string[i],string[i+1]=string[i+1],string[i]
            
            # Incrementing by 2 because we have already worked with two indexes
            i += 2
            
        else:
            
            # If No, move to the next index
            i += 1
    j += 1
    
# Converting final list into string and printing
print(''.join(string))
