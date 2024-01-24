# 1+3+5+7...+(2n+1)

def recursion(n):
    if n == 0:
        return 1
    else:
        return recursion(n-1) + (2*n + 1)

print(recursion(3))