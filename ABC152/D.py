N = int(input())

ans = 0
headN = str(N)[0]
tailN = str(N)[-1]
digitN = len(str(N))

for i in range(1, N+1):
    headB = str(i)[-1]
    tailB = str(i)[0]
    digiti = len(str(i))

    if(headB == 0):
        break
    
    if(digitN == digiti):
        ans += 1  # always i <= N

    elif(digitN > digiti):
        diffDigit = digitN - digiti
        Num = int(str(N)[1:-1])

        if(headN < headB):
            Num = int(str(min(int(str(N)[1])-1, 0)) + str(N)[2:-1])
            if(strNum == ''):
                Num = 0
        if(tailN < tailB):
            Num = int(str(str(N)[1:-2]+ min(int(str(N)[-1])-1,0)))
            if(strNum == ''):
                Num = 0


        ans += strNum

print(ans)
