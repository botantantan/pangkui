"""
Input sample:
8
10 2 0 5 7 2 5 2
Sample output:
0:1
2:3
5:2
7:1
10:1
Test data: sample is equivalent; service age is all 0; service age is entered in descending order
"""

n = int(input()) # ada brp employee
s = sorted(list(map(int,input().split()))) # service age dari tiap employee

# karena ada sorted, s = [0, 2, 2, 2, 5, 5, 7, 10]

# map itu buat ngejalanin fungsi buat tiap item dari suatu iterable 
# kalo disini fungsi nya itu int(), iterable input().split()
# jadi dia convert setiap item di input().split() dari string ke integer

z = {} # z itu dictionary, format nya key:value

for i in range(0,len(s)): # loop sebanyak panjang dari s
    if s[i] not in z: # kalo s[i] gk ada di z
        z[s[i]] = 1 # buat item baru di z dengan key s[i] dan value 1
    else : # kalo s[i] ada di z
        z[s[i]] = z[s[i]] + 1 # item dengan key s[i] valuenya ditambah 1

for name in z:
    print("{}:{}".format(name,z[name]))