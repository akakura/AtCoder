A, B, K = map(int, input().split())

if(A < K):
    print(0, max(0, B-K+A))
else:
    print(A-K, B)
