"""
Input sample:
HELLO World!
Sample output:
4
"""

s = input()

count = 0
for c in s:
  if (c not in "aiueoAIUEO" and c.isupper()):
    count += 1

print(count)