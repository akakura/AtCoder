import numpy as np
H, N = map(int, input().split())
A = []
B = []
C = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(float(a/b))
maxC = max(C)
print(H)

maxMana = int((H/max(C) +1) * maxC)
dp = np.zeros((maxMana+1, N+1))
flag = False

for j in range(1, maxMana+1):
    for i in range(1, N+1):
        cand1 = dp[j-1][i]
        cand2 = dp[j-B[i-1]][i-1] + A[i-1] if j >= B[i-1] else dp[j]
        cand3 = dp[j-B[i-1]][i] + A[i-1] if j >= B[i-1] else dp[j][i]

        dp[j][i] = max(cand1, cand2, cand3)
        if(dp[j][i] >= H):
            flag = True
        if(flag):
            break
    if(flag):
        break

print(dp)
print(j)

