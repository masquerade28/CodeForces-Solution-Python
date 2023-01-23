forces = int(input())
L = []
for i in range(forces):
    L.append([int(i) for i in input().split()])

if L[0][0] + L[1][0] + L[2][0] == 0 and L[0][1] + L[1][1] + L[2][1] == 0 and L[0][2] + L[1][2] + L[2][2] == 0 :
    print("YES")
else :
    print("NO")
