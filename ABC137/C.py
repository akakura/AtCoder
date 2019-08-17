N = int(input())
s = ['']*N
 
for i in range(N):
	str = input()
	s[i] = ''.join(sorted(str))
 
s.sort()
ans = 0

#for i in range(N):
i = 0
while (i < N):
	current = s[i]
	same = 1
	while(i < N-1):
		if(s[i+1] == current):
			i += 1
			same += 1
		else:
			break

	ans += same * (same - 1)//2
	#print(i, same, ans)
	i += 1

print(ans)
