X = int(input())

for A in range(-118, 120):
    for B in range(-119, 119):
        A5 = pow(A,5)
        B5 = pow(B,5)
        if( (A5-B5) == X):
            ans = str(A) + ' ' + str(B)
            break

print(ans)