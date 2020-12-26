"""
Input sample:
Let's go to room 209.
Sample output:
5
"""

s = input()

s = s.split()
count = 0
for word in s:
  count += 1
print(count)