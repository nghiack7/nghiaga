import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
def find_alphabe(x):
    dai = len(s)
    a = []
    b = []
    for item in s:
        if item not in a:
            a.append(item)
    for item in a:
        sodem = 0
        for i in range(len(s)):
            if str(s[i]) == str(item):
                sodem += 1
        b.append([item, sodem])
    return b
a =find_alphabe(s)
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i][1] < a[j][1]:
            a[i],a[j] = a[j],a[i]
        elif a[i][1] == a[j][1]:
            if a[i][0] > a[j][0]:
                a[i],a[j] = a[j],a[i]
for i in range(0,3):
    print(f"{a[i][0]} {a[i][1]}")
