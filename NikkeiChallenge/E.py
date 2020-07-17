N, K = map(int,input().split())

if(K > N):
    print(-1)
elif(K == 1):
    for i in range(N):
        list = [K+i, K+N+i, k+2*N+i]
        print(*l, sep=' ')
else:
    for i in range(N):
        list = [K+i, K+N+i, k+2*N+i]
        print(*l, sep=' ')