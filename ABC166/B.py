N, K = map(int, input().split())
ans = [1]*N
for i in range(K):
    d = int(input())
    okashi = [int(num) for num in input().split()]
    
    for j in range(d):
        ans[okashi[j]-1] = 0

print(sum(ans))