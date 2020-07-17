N = int(input())
P = [int(i) for i in input().split()]

minNum = P[0]
ans = 0
for i in range(len(P)):
    if(P[i] <= minNum):
        ans += 1
        minNum = P[i]
    
print(ans)