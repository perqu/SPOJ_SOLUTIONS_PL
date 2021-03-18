def GCD(a, b): #NWD
    if b > 0:
        return GCD(b, a%b)
    return a

def LCM(a,b): #NWW
    return (a*b)//(GCD(a,b))

n = int(input())
for i in range(n):
    g1,g2 = input().split()
    print(LCM(int(g1),int(g2)))