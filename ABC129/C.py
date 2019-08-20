N, M = map(int,input().split())
 
broken = [N+1]*(M+1)
ans = [0]*(N+1)
broken_pointer = 0
for i in range(M):
    a = int(input())
    broken[i] = a
 
ans[0] = 1
if(broken[0] == 1):
    ans[1] = 0
    broken_pointer += 1
else:
    ans[1] = 1
 
for i in range(2,N+1):
    if (broken[broken_pointer] == i):
        ans[i] = 0
        broken_pointer += 1
    else:
        ans[i] = ans[i-1] + ans[i-2]
    
 
print(ans[N]%1000000007)
N, M = map(int,input().split())

broken = [N+1]*(M+1)
ans = [0]*(N+1)
broken_pointer = 0
for i in range(M):
    a = int(input())
    broken[i] = a

ans[0] = 1
if(broken[0] == 1):
    ans[1] = 0
    broken_pointer += 1
else:
    ans[1] = 1

for i in range(2,N+1):
    if (broken[broken_pointer] == i):
        ans[i] = 0
        broken_pointer += 1
    else:
        ans[i] = ans[i-1] + ans[i-2]
    

print(ans[N]%1000000007)
