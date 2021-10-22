import numpy
nm = input().split()
n = int(nm[0])
m = int(nm[1])
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
a = numpy.array(lst)
a.shape = (n,m)
print(numpy.mean(a, axis =1))
print(numpy.var(a, axis= 0))
stda =numpy.std(a, axis= None)
print(round(stda, 11))