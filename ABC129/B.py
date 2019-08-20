N = int(input())
 
W = list(map(int, input().split()))
 
S1 = 0
S2 = sum(W)
diff = S2-S1
for i in range(N):
    newdiff = abs(S2-S1)
    S1 += W[i]
    S2 -= W[i]
    if(newdiff < diff):
        diff = newdiff
 
print(diff)
N = int(input())

W = list(map(int, input().split()))

S1 = 0
S2 = sum(W)
diff = S2-S1
for i in range(N):
    newdiff = abs(S2-S1)
    S1 += W[i]
    S2 -= W[i]
    if(newdiff < diff):
        diff = newdiff

print(diff)
