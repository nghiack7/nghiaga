import numpy
nm = input().split()
n = int(nm[0])
m = int(nm[1])
lsta = []
lstb = []
for i in range(n):
    lsta.append(list(map(int, input().split())))
for i in range(n):
    lstb.append(list(map(int, input().split())))
a = numpy.array(lsta)
b = numpy.array(lstb)
a.shape = (n,m)
b.shape = (n,m)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.floor_divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))