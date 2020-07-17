def GCD(a, b):
    r = a % b
    while(r!=0):
        a = b
        b = r
        r = a % b
    
    return b

def main():
    ans = 0 
    K = int(input())
    for i in range(1, K+1):
        for j in range(1, K+1):

            if(i == 1 or j == 1):
                gcd1 = 1
            elif(i < j):
                gcd1 = GCD(j, i)
            else:
                gcd1 = GCD(i, j)
            for k in range(1, K+1):
                ans += GCD(gcd1, k)

    print(ans)



if __name__ == main():
    main()