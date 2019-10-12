import math
N, M = map(int,input().split())

A = [int(x) for x in input().split()]
A.sort(reverse=True)

# first coupon
max = 0
newval = A[max] >> 1
A[max] = newval

if(M==1):
    print(sum(A))
else:
    #   second coupon

    if(M==2):
        print(sum(A))

    else:

    # rest of coupons
    for i in range(2, M):
        if(A[max] >= A[i]):
            A[max] = A[max] >> 1
            if(A[max] < A[i]):
                max = i
        else:
            A[i] = A[i] >> 1
            if(A[i] > A[max]):
                max = i

    print(sum(A))
    