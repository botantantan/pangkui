"""
Input sample:
6
2 8 10 1 9 10
Sample output:
10 2
"""

n = input()
list_temp = input().split()
list_num = list()
for i in list_temp:
  list_num.append(int(i))

index = 0
for i in range(len(list_num)):
  if (list_num[i] == max(list_num)):
    index = i
    break

print("{} {}".format(max(list_num), index))


n=int(input())
lst=input().split()

if 1<n<=10 and n==len(lst):
  lst1=[int(x) for x in lst]
  print("%d %d"%max(lst1),lst1.index(max(lst1))))