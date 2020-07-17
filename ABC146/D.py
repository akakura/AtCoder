N = int(input())

for i in range(*)
X, Y= map(int, input().split())

if((2*Y-X)%3 != 0 or (2*X-Y)%3 != 0):
    print("0")
else:
    a =  int((2*Y-X) / 3)
    b =  int((2*X-Y) / 3)

    if(a <= 0 or b <= 0):
        print("0")
    else:
        numerator = [b + k + 1 for k in range(a)]
        denominator = [k + 1 for k in range(a)]

        for p in range(2,a+1):
            pivot = denominator[p - 1]
            if pivot > 1:
                offset = (b) % p
                for k in range(p-1,a,p):
                    numerator[k - offset] /= pivot
                    denominator[k] /= pivot

        result = 1
        for k in range(a):
            if numerator[k] > 1:
                result *= int(numerator[k])

        print(result % (10**9+7))