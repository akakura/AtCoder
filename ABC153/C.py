N, K = map(int, input().split())
H = [int(i) for i in input().split()]

H.sort(reverse=True)

Attack = H[K:]
print(sum(Attack))