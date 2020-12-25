m = 1
while (True):
    if (m%5==1 and m%6==5 and m%7==4 and m%11==10):
        print(m)
        break
    m = m + 1