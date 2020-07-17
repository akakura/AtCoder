import numpy as np
N = int(input())

tes = np.zeros((N, N))
cnt = np.zeros(N)
for i in range(N):
    num = int(input())
    for j in range(num):
        x, y =  map(int, input().split())
        tes[i][x-1] = y*2-1
        cnt[x-1] += 1

cnt = np.where(cnt < 1, 1, cnt)
#print(cnt)
ans = 0
arr = np.zeros(N)
sub = np.ones(N)
for i in range(2**N):
    arr[N-1] += 1
    for j in range(N-1):
        if(arr[N-1-j] == 2):
            arr[N-1-j] = 0
            arr[N-2-j] += 1
        if(arr[0] == 2):
            arr[0] = 0
    arr = arr*2-sub

    calc1 = np.dot(arr, tes)/cnt    
    calc2 = np.sum(calc1)
    if(calc2 > ans):
        ans = calc2


print(int(ans))