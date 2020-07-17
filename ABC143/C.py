N = int(input())
S = input()

ans = 0
color = ''
for i in range(N):
    if(S[i] != color):
        ans += 1
    color = S[i]

print(ans)