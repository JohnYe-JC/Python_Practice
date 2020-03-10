n = int(input())
a = 1
b = 1
m = 0
for i in range(0, n):
    if i == 0 or i == 1:
        print(1)
    else:
        print(a + b)
        m = b
        b = a + b
        a = m
