
n = int(input())

def cre_fibo(n):
    a = []
    if 0 <=n <=2:
        for i in range(0,n+1):
            a.append(i)
        return a
    else:
        a = [0,1]
        for i in range(2,n+1):
            a.append(a[i-1]+a[i-2])
        return a
fibonacy = cre_fibo(n)
print("day so fibonacy can tim la {}",format(fibonacy))
print("so thu n trong day fibonacy la: {}".format(fibonacy[n]))