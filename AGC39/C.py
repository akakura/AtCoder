N = int(input())
X = input()

numX = int(X, 2)

if(N%2 == 1):
    ans = N*2*(numX+1)
    for i in range(N//6 + 1):
        comp1 = ("1"*(2*i+1) + "0"*(2*i+1)) * (N//(2*(2*i+1))) + "1"*(2*i+1)
        comp2 = ("0"*(2*i+1) + "1"*(2*i+1)) * (N//(2*(2*i+1))) + "0"*(2*i+1)

        if(int(X)-int(comp1)>0):
            ans = ans - (N*2)*2 + 2*((2*i+1)*2)
        elif(int(X)-int(comp2)>0):
            ans = ans - (N*2)*1 + 2*((2*i+1)*2)

else:
    ans = N*2*(numX+1)
    for i in range(N//6 + 1):
        comp1 = ("1"*(2*i+2) + "0"*(2*i+2)) * (N//(2*(2*i+2))) + "1"*(2*i+2)
        comp2 = ("0"*(2*i+2) + "1"*(2*i+2)) * (N//(2*(2*i+2))) + "0"*(2*i+2)

        if(int(X)-int(comp1)>0):
            ans = ans - (N*2)*((2*i+2)*2) + ((2*i+2)*2)*(2*i+2)*2
        elif(int(X)-int(comp2)>0):
            ans = ans - (N*2)*((2*i+2)*2) + ((2*i+2)*2)*(2*i+2)*1

print(ans%998244353)