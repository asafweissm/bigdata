def n():
    return 1

def pnlprod(to):
    prod = 1
    for i in range(1, to+1):
        prod *= ((1-2**(-i))**(-1))
    return prod
    
def p(n, l):
    s = 0
    for j in range(0, l): # 0 ... l-1
        s += (-1)**j * 2**(-0.5*j*(j-1)) * (1 - 2**(j-l))**n * pnlprod(j) * pnlprod(l - 1 - j)
    return s

if __name__ == '__main__':
    for i in range(20):
        print(p(i, 1))
    for i in range(20):
        print(p(i, 2))
