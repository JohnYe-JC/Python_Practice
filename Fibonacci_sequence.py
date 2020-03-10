n = int(input())
i = 3
a = 1
b = 1
c = 0
print(a)
print(b)
while i <= n:
    c = a + b
    print(c)
    a = b
    b = c
    i += 1
