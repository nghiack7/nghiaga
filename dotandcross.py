import numpy

n = int(input())
a=[]
b=[]
for i in range(n):
    a.append(list(map(int,input().split())))
for _ in range(n):
    b.append(list(map(int,input().split())))
ar = numpy.array(a)
br = numpy.array(b)
ar.shape = (n,n)
br.shape = (n,n)
print(numpy.dot(ar,br))


