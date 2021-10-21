import numpy
numpy.set_printoptions(legacy='1.13')
in_a = [float(item) for item in input().split()]
A = numpy.array(in_a)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))

 