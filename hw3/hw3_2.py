n = int(input("n: "))

product = 1
for i in range(1, n):
    if (i%2 == 0):
        product *= i

if (n<3):
    print("gk ad out boi")
else:
    print(product)
