"""
Input example 1:
Here is a set of inputs. E.g:
Mary
arMy
Output sample 1:
The corresponding output is given here. E.g:
yes
Input example 2:
Here is a set of inputs. E.g:
hello 114
114 hello
Output sample 2:
The corresponding output is given here. E.g:
yes
Input example 3:
Here is a set of inputs. E.g:
Wellcom
mocllew
Sample output 3:
The corresponding output is given here. E.g:
no
"""

s=list(input())
m=list(input())
count=0
for i in range(len(s)):
    if s.count(s[i])==m.count(s[i]):
        count+=1
if(s == m):
    print("no")
elif count == len(s):
    print("yes")
else:
    print("no")
