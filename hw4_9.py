"""
Z: 0 1 2 3 4 5 6 7 8 9 10
M: 1 0 X 9 8 7 6 5 4 3 2

Input example 1:
4
320124198808240056
12010X198901011234
110108196711301866
37070419881216001X
Output sample 1:
12010X198901011234
110108196711301866
37070419881216001X
Input example 2:
2
320124198808240056
110108196711301862
Output sample 2:
All passed
"""

def check_id(id, count):
  w = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
  m = "10X98765432"

  if (id[0:16].isdigit() == False):
    return print(id)
  
  sum = 0
  for i in range(17):
    sum += int(id[i]) * w[i]
  
  if (id[17] == m[sum%11]):
    return count+1
  else:
    return print(id)
  
n = int(input())
id_list = list()
count = 0

for i in range(n):
  id = input()
  id_list.append(id)

for id in id_list:
  count = check_id(id, count)

if (count == n):
  print("All passed")