N, M = map(int, input().split())
cons = [int(item) for item in input().split()]

ans = N - sum(cons)
if(ans < 0):
        ans = -1

print(ans)