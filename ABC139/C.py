import numpy as np 
N = int(input())
H = [int(x) for x in input().split()]
L = H[0:N] + [-1]

print(H)
print(L)
Hp = np.array(H)
Lp = np.array(L)

line = list(map(lambda x: (1,0)[x<0], Hp-Lp))
id= [i for i, x in enumerate(line) if x == 0]
#print(indexes) 
id2 = [0] + id[0:N]
print(max(id-id2))

ans = 0
for i in range(N):
    count = 0
    temp = H[i]
    while(True):
        if(i==N-1):
            break
        elif(temp >= H[i+1]):

                count += 1
                i += 1
        else:
            break
 
    if(count > ans):
        ans = count
        if(N-i < ans):
            break
 
print(ans)
 