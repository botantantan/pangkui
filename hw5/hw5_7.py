"""
Input example 1:
level
Output sample 1:
level
Yes
Input example 2:
1 + 2 = 2 + 1 =
Output sample 2:
1 + 2 = 2 + 1 =
No
"""

str = input()
flag = 1
for i in range(0,int(len(str)/2)):
    if(str[i] != str[len(str) - 1 - i]):
        flag = 0
if(flag == 1):
    print(str)
    print("Yes")
else:
    print(str)
    print("No")

