"""
Input sample:
free82jeep5
Sample output:
825
"""

s = input()
list_out = list()

for i in s:
  if (i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
    list_out.append(int(i))

for i in range(len(list_out)):
  if (i == len(list_out)-1):
    print(list_out[i])
  else:
    print(list_out[i], end = "")