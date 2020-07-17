N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

ans = 0
# count for 0 ~ K
for i in range(N-K):
    if(T[i] == 'r'):
        point = P
    elif(T[i] == 's'):
        point = R
    elif(T[i] == 'p'):
        point = S
    else: # already used
        point = 0
    ans += point

    if(T[i+K] == T[i]):
        T[i+K] = 'n'

# count for K ~ N
for i in range(N-K, N):
    if(T[i] == 'r'):
        point = P
    elif(T[i] == 's'):
        point = R
    elif(T[i] == 'p'):
        point = S
    else: # already used
        point = 0
    ans += point

print(ans)