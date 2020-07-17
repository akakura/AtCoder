N, M = map(int, input().split())
H = [int(num) for num in input().split()]
ans = [1] * N

for i in range(M):
    A, B = map(int, input().split())
    if(H[A-1] > H[B-1]):
        ans[B-1] = 0
    elif(H[B-1] > H[A-1]):
        ans[A-1] = 0
    else:
        ans[A-1] = 0
        ans[B-1] = 0

print(sum(ans))