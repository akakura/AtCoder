N = int(input())
S = input()
output = ""
for i in range(len(S)):
    StoN = ord(S[i])
    StoN += N
    if(StoN >= 91):
        StoN -= 26
    output += chr(StoN)

print(output)