import functools

def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a%b)

def multiple(a, b):
    return a*b // euclid(a, b)

def lcm(nums):
        return functools.reduce(multiple, nums)

N = int(input())
A = list(map(int, input().split()))
NumLCM = lcm(A)
ans = 0
for i in range(len(A)):
    ans += NumLCM // A[i]

print(ans % (10**9+7))