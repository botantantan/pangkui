n = int(input())
total = float(1)
a = float(2)
b = float(3)

minus = float(0)

for i in range (n-1):
    if (i%2==0):
        minus = -1
    else:
        minus = 1
    
    total = total + (minus*a/b)
    a = a + 1
    b = b + 2

total = round(total, 3)
print(total)