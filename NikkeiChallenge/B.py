N = int(input())
S = [int(i) for i in input().split()]

result = 0
for i in range(len(S)):
    if(i%2 == 0):
        if(S[i] == "L"):
            result = 1
            break
    elif(i%2 == 1):
        if(S[i] == "R"):
            result = 1
            break


if(result == 0):
    print("Yes")
else:
    print("No")