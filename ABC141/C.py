N, K, Q = map(int,input().split())

Point = [0]*N
for i in range(Q):
    Correct = int(input())
    Point[Correct-1] += 1

for i in range(N):
    if(Point[i] > Q-K):
        print("Yes")
    else:
        print("No")
