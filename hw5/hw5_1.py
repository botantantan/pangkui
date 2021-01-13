"""
Input sample:
143 174 119 127 117 164 110 128
Sample output:
143 174 164
"""

list_num = input().split()

total = 0
for i in list_num:
  total = total + int(i)
avg = total/len(list_num)

for i in list_num:
  if (int(i) > avg):
    print(i, end = " ")