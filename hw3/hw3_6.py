n = int(input())

for i in range (1, n+1):
    for j in range (1, n+1):
        if (j == n):
            if (i < j or i == j):
                print("   {}".format(i))
            else:
                print("   {}".format(j))
        else:
            if (i < j or i == j):
                print("   {}".format(i), end = "")
            else:
                print("   {}".format(j), end = "")