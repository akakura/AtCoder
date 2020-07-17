import math
A, B, X= map(int, input().split())

MaxN = X // A
if(MaxN == 0):
    print(0)
else:
    digMaxN = int(math.log10(MaxN)+1)
    MinN = (X-B*digMaxN)//A
    if(MinN <= 0):
        digMinN = 0
    else:
        digMinN = int(math.log10(MinN)+1)

    for i in range(digMinN, max(digMinN+1, digMaxN)+1):
        res = X - B * i
        N = res // A

        digN = int(math.log10(N)+1)
        if(digN == i):
            break
            

    if(N > 10**9):
        N = 10**9

    print(N)