import numpy as np

def updateline(l, r, N, b):
    dp = np.array([0]*(N+1))
    for i in range(N+1):
        if(sum(r[:i]) < b):
            break
        else:


def main():
    N, B1, B2, B3 = map(int,input().split())
    B = [B3]#, B2, B1]
    l = np.array([[0]*N]*N)
    r = np.array([[0]*N]*N)
    horiz = np.array([0]*N)
    vert = np.array([0]*N)

    for i in range(N):
        l[i] = [int(x) for x in input().split()]
        horiz[i] = sum(l[i])
        vert += l[i]

    for i in range(N):
        r[i] = [int(x) for x in input().split()]

# search & update from B3, B2, then B1
    for b in B:
        minhoriz = np.min(horiz)
        minvert = np.min(vert)
        if(min(minhoriz, minvert) > b):
            break
        elif(max(minhoriz, minvert) < b):
            break
        else:
            if(minhoriz <= minvert):
                cand = np.argmin(minhoriz)
                updateline(l[cand], r[cand], N, b)
            else:
                cand = np.argmin(minvert)
                updateline(l[:,cand], r[:,cand], N, b)

    for i in range(N):
        print(' '.join(map(str, l[i])))

if __name__ == '__main__':
    main()