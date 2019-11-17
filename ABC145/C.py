import math
N = int(input())

x = [0]*N
y = [0]*N
for i in range(N):
    x[i], y[i] = map(int, input().split())

sum = 0
M = math.factorial(N-1)
for i in range(N):
    for j in range(N):
           sum += math.sqrt((x[j]-x[i])*(x[j]-x[i]) + (y[j]-y[i])*(y[j]-y[i])) * M


print(sum/math.factorial(N))