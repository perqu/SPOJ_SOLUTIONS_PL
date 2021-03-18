def multiplication(a,b):
    return a*b

n = int(input())
for i in range(n):
    a,b = input().split()
    print(multiplication(int(a), (int(b))))