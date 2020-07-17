N = int(input())
X = [int(i) for i in input().split()]

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        ans += X[i] ^ X[j]

print(ans%(10**9+7))