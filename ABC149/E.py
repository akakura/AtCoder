N, M = map(int, input().split())
A = [int(i) for i in input().split()]

list.sort(A, reverse=True)

ans = 0
pos1 = 0 # pointer in Array A
pos2 = 0 # always pos1 <= pos2
CanReverse = True
for i in range(M):
    ans += A[pos1] + A[pos2]
    if(pos1 != pos2):
        
    if(i % 3 == 0):
        pos2 += 1
        if(pos2 >= N):
            pos2 = N-1
            pos1 += 1

    elif(i % 3 == 2):
        if(A[pos1+1]+A[pos2] > A[pos1]+A[pos2+1]):
            pos1 += 1
            if(pos1 >= N):
                break
        else:
            pos2 += 1
            if(pos2 >= N-1):
                pos2 = N-1
                pos1 += 1
                if(pos1 >= N):
                    break
    #else:
        # do nothing
        # just swap Right & Left

print(ans)