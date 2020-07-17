import numpy as np

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

numA = np.array(A)
A.sort()
B.sort()
An = np.array(A)
Bn = np.array(B)
if(np.min(Bn-An) < 0):
  print("No")

else:
  order = numA.argsort()[::-1]
  cnt = 0
  for i in order:
    if(A[i] > B[i]):
      cnt += 1
  if(cnt > N-2):
    print("No")
  else:
    print("Yes")
