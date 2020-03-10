n = int(input())
i = 3
a = 1
b = 1
temp = 0
print(a)
print(b)
while i <= n:
    print( a + b )
    temp = b
    b = a + b
    a = temp
    i += 1
