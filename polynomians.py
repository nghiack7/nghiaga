import numpy
def ham(x):
    a = []
    for i in x:
        if i is not int:
            a.append(float(i))
        else: a.append(int(i))
    return a
p = input().split()
print(p)
a = ham(p)
x = int(input())
P = numpy.polyval(a, x)
print(P)
print(numpy.poly(a))