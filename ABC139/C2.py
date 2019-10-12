N = int(input())
H = [int(x) for x in input().split()]
 
ans = 0
current = 0
for i in range(N):
    if(i == N-1):
        if(current > ans):
            ans = current
        break
    if(H[i] >= H[i+1]):
        current += 1
    else:
        if(ans < current):
            ans = current
        current = 0
 
print(ans)
 