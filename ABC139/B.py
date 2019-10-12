import math
A, B = map(int,input().split())

if(B==1):
    print("0")
elif(A >= B):
    print("1")
else:
    print(math.ceil((B-A)/(A-1))+1)

print(ans)