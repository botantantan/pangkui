"""
Input sample:
10 3 2 -1 5 3 4 3 0 3 2
Sample output:
3 4
"""

import statistics

list_num = input().split()

del list_num[0]

mode = statistics.mode(list_num)
count = 0
for i in list_num:
  if (i == mode):
    count = count + 1

print("{} {}".format(mode, count))


