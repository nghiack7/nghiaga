def demsotrongchuoi(s):
    a = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            a += 1
        else: break
    return a + 1

def count(s):
    b= []
    while True:
        for _ in range(len(s)):
            if len(s) == 0:
                return b
            else:
                x = demsotrongchuoi(s)
                b.append(x)
                s = s[x:]
                print(x,b,s)
def demsub(a):
    sub = 0
    for i in range(len(a)-1):
        sub += min(a[i],a[i+1])
    return sub
a = count("100010001001")
demnhiphan = demsub(a)
print(demnhiphan)