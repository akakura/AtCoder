N, X = map(int,input().split())
 
L = input().split()
pos = 0
ans = 1
for i in range(N):
  pos += int(L[i])
  if(pos <= X):
    ans +=1
  else:
    break
  
print(ans)
N, X = map(int,input().split())

L = input().split()
pos = 0
ans = 1
for i in range(N):
  pos += int(L[i])
  if(pos <= X):
    ans +=1
  else:
    break
  
print(ans)