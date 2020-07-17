N = int(input())
D = [int(i) for i in input().split()]

ans = 0
sumD = D[0]
for i in range(1, N):
    ans += sumD * D[i]
    sumD += D[i]


print(ans)