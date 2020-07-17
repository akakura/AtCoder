S = input()
K = int(input())

S += "1"
l = len(S)
pair = []
current = S[0]
seq = 1
for i in range(1, l):
    if(i == l):
        pair.append(seq)
    elif(S[i] == current):
        seq += 1
    else:
        pair.append(seq)
        seq = 1
        current = S[i]

ans = 0
#print(pair)
if(len(pair) == 1):
    ans += (K * pair[0])//2
elif(S[0] != S[l-2]):
    for i in range(len(pair)):
        ans += K * (pair[i]//2)
else:
    for i in range(1, len(pair)-1):
        ans += K * (pair[i]//2)
    ans += (pair[0]//2) + (pair[i+1]//2) + ((pair[0]+pair[i+1])//2)*(K-1)

print(ans)