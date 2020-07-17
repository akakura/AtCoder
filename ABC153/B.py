H, N = map(int, input().split())
A = [int(i) for i in input().split()]

all = sum(A)

if(all >= H):
    print("Yes")
else:
    print("No")