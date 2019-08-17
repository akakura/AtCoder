N, M = map(int, input().split())
Pay = [0]*N
Day = [0]*N

for i in range(N):
    a, b = map(int, input().split())
    Day[i] = a
    Pay[i] = b

dp = [[0]*(M+1)]*(N+1)

for i in range(N):
    for day in range(M+1):
        if (day >= Day[i]):
            dp[i+1][day] = max(dp[i][day-Day[i]] + Pay[i], dp[i][day])
        else:
            dp[i+1][day] = dp[i][day]

for i in range(N):
    print(dp[i])

print(dp[N][M])
