"""
Input sample:
mississippi
s p
Input sample:
9 p
8 p
6 s
5 s
3 s
2 s
"""

s = input()
c1, c2 = input().split()

list_c = list((c1, c2))
list_out = list()

for c in list_c:
  for i in range(len(s)):
    if (c == s[i]):
      list_out.append("{} {}".format(i, c))

for out in list_out[::-1]:
  print(out)