"""
Input sample:
free82jeep5
Sample output:
825
"""

s = input()
s_out = ""

for i in s:
  if (i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0'):
    s_out = s_out + i

if (s_out[0] == "0"):
  s_out = s_out.replace("0", "", 1)

print(s_out)