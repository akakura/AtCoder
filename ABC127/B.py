r, D, xinit= map(int, input().split())

x = xinit

for i in range(10):
    x = r*x - D
    print(x)
