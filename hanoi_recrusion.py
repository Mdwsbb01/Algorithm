#recrusion example: hanoi
def haNoi(n, a, b, c):
    if n > 0:
        haNoi(n-1, a, c, b)
        print("moving from %s to %s" % (a, c))
        haNoi(n-1, b, a, c)

haNoi(3, 'A', 'B', 'C')

#equation:h(n) = h(n-1) + 1 + h(n-1)
#h(x) = 2h(x-1) + 1 ~~ 2^n
#https://github.com/Mdwsbb01/Algorithm.git