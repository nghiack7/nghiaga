import numpy

a = [int(item) for item in input().split()]
b =  [int(item) for item in input().split()]
ar = numpy.array(a)
br = numpy.array(b)
print(numpy.inner(ar,br))
print(numpy.outer(ar,br))