N = int(input())
S = input()

m = N//2
if(N%2 != 0 or S[:m] != S[m:]):
    print("No")
else:
    print("Yes")