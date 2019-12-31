N, T = map(int, input().split())


C = [[0,0]*N]
for i in range(N):
    A, B = map(int, input().split())
    C[i] = [A, B]
print(C)
sorted(C, reverse=True, key=lambda x: x[1])
print(C)