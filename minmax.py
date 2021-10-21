import numpy


nm = input().split()
n = int(nm[0])
m = int(nm[1])
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
a = numpy.array(lst)
a.shape = (n,m)
b = numpy.min(a, axis = 1)
print(numpy.max(b))
