Len, Pos = map(int, input().split())
Left = -1000000
Right = 1000000
 
candL = max(Pos-Len+1, Left)
candR= min(Pos+Len-1, Right)
 
cand = [x for x in range(candL, candR+1)]
ans = ''
 
for s in cand:
  ans += str(s) + ' '
  
print(ans.rstrip())