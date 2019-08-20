N = int(input())
SN = []
for i in range(N):
  s, n =input().split()
  SN.append([s, int(n), i])
 
SN.sort()
#print(SN)
 
start = 0
while (start < N-1):
  for i in range(start, N):
    search = SN[start][0]
    while(SN[i][0] == search):
      end = i
      if(i<N-1):
        i = i+1
      else:
        end = i
        break
        
  SNpart = SN[start:min(end+1, N)]
  #print(SNpart)
  SNpart.sort(key=lambda x:-x[1])
  SN[start:min(end+1, N)] = SNpart
 
  #print(SN[start:end+1])
  start = end+1
 
for i in range(N):
  print(SN[i][2]+1)