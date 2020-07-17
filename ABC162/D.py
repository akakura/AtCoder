N = int(input())
S = input()

ans = 0
for i in range(N-2):
    I = S[i]
    resStr = 'RGB'.replace(I,'')
    ans += len(S[i+1:].replace(I,'').replace(resStr[0],'')) * len(S[i+1:].replace(I,'').replace(resStr[1],''))

    for j in range(1, (N-1-i)//2):
        if(S[i+j] != S[i+2*j] and S[i+j] != I and S[i+2*j] != I):
            ans -= 1
     
print(ans)