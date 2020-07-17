import bisect 

N = int(input())
L = [int(i) for i in input().split()]

L.sort()

ans = 0
for i in range(N-2):
    small = L[i]

    for j in reversed(range(i+2, N)):
      large = L[j]
      target = large - small + 1
      pos = bisect.bisect_left(L[:j], target)
      # print(i, j, pos)
      #if(i <= pos):
      ans += j- max(i+1, pos)

print(ans)