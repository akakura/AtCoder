N, K  = map(int, input().split())

ans = 0
for i in range(K, N+2):
    minN = (i-1) * i //2
    maxN = (2*N-i+1) * i //2
    ans += (maxN - minN + 1) % (pow(10,9)+7)

print(ans % (pow(10,9)+7))