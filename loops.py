if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(i))
    b = list(map(lambda x: x**2, a))
    for item in b:
        print(int(item))