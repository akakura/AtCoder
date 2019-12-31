N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()


MaxHand = max(R,S,P)
MinHand = min(R,S,P)

ans = 0
for i in reversed(len(T)-K):
    if(T[i] != T[i+K]):
        if(T[i] == 'r'):
            point = P
        elif(T[i] == 's'):
            point = R
        else:
            point = S
        ans += point

for i in range(len(T)-K, len(T)):
        if(T[i] == 'r'):
            point = P
        elif(T[i] == 's'):
            point = R
        else:
            point = S
        ans += point

print(ans)