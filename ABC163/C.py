N = int(input())
Mgr = [int(num) for num in input().split()]
sub = [0]*N

for i in range(len(Mgr)):
    sub[Mgr[i]-1] += 1

for i in range(N):
    print(sub[i])
