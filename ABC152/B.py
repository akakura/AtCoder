a, b= input().split()

ab = a * int(b)
ba = b * int(a)

if(int(a) > int(b)):
    print(ba)
else:
    print(ab)