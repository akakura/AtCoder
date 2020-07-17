H = int(input())

ans = 0
attack = 1
while(True):
    ans += attack
    H = H //2
    attack = attack *2

    if(H==0):
        break


print(ans) 