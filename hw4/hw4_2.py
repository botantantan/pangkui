"""
Input example 1:
m
programming
Output sample 1:
index = 7
Input example 2:
a
1234
Output sample 2:
Not Found
"""

c = input()
s = input()

index = -1
for i in range(len(s)):
  if (s[i] == c):
    index = i

if (index == -1):
  print("Not Found")
else:
  print("index={}".format(index))