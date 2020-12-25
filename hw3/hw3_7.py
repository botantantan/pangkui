import math

a, b = input().split()
a = int(a)
b = int(b)

tinggi = int(math.ceil(float((b-a+1)/5)))
total = 0

for i in range (tinggi):
    for j in range (5):
        if (i == tinggi-1 and j == 4):
            if (a > -10 and a < 0):
                print("   {}".format(a), end = "")
            elif (a > -100 and a <= -10):
                print("  {}".format(a), end  = "")
            elif (a == -100):
                print(" {}".format(a), end = "")
            elif (a >= 0 and a < 10):
                print("    {}".format(a), end = "")
            elif (a >= 10 and a < 100):
                print("   {}".format(a), end = "")
            elif (a == 100):
                print("  {}".format(a), end = "")
        elif (j == 4):
            if (a > -10 and a < 0):
                print("   {}".format(a))
            elif (a > -100 and a <= -10):
                print("  {}".format(a))
            elif (a == -100):
                print(" {}".format(a))
            elif (a >= 0 and a < 10):
                print("    {}".format(a))
            elif (a >= 10 and a < 100):
                print("   {}".format(a))
            elif (a == 100):
                print("  {}".format(a))
        else:
            if (a > -10 and a < 0):
                print("   {}".format(a), end = "")
            elif (a > -100 and a <= -10):
                print("  {}".format(a), end = "")
            elif (a == -100):
                print(" {}".format(a), end = "")
            elif (a >= 0 and a < 10):
                print("    {}".format(a), end = "")
            elif (a >= 10 and a < 100):
                print("   {}".format(a), end = "")
            elif (a == 100):
                print("  {}".format(a), end = "")
        
        total = total + a
        a = a + 1
        
        if (a > b):
            print()
            break
            
print("Sum = {}".format(total))