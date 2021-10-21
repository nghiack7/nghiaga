import numpy

nmp = input().split()
n = int(nmp[0])
m = int(nmp[1])
p = int(nmp[2])
lstn=[]
lstm=[]
for _ in range(n):
    lstn.append(list(map(lambda x: int(x), input().split())))
for _ in range(m):
    lstm.append(list(map(lambda x: int(x), input().split())))
arr_m = numpy.array(lstm)
arr_n = numpy.array(lstn)
arr_m.shape = (m,p)
arr_n.shape = (n,p)
print(numpy.concatenate((arr_n,arr_m), axis=0))