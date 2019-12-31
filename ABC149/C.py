
def FindPrime(X):
    while(True):
        if isPrime(X):
            break
        else:
            X += 1

    print(X)

def isPrime(X):
    ans = True
    for i in range(2, X//2):
        if(X % i == 0):
            ans = False
            break
    return ans

if __name__ == '__main__':
    X = int(input())
    FindPrime(X)