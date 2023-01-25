n,t = map(int,input().split())
string = list(str(input()).upper())
j = 0
while j < t:
    i = 0
    while i < len(string)-1:
        if string[i] == "B" and string[i+1] == "G":
            string[i],string[i+1]=string[i+1],string[i] 
            i += 2
        else:
            i += 1
    j += 1
print(''.join(string))
