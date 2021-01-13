"""
Input sample:
Here is a set of inputs. E.g:
Bee
E
Sample output:
The corresponding output is given here. E.g:
result: B
"""

a=input().strip()
b=input().strip()
print("result:",a.replace(b.upper(),'').replace(b.lower(),''))

str1=input().strip()
x=input().strip()
str2=''
if len(str1) !=0:
  for ch in str 1:
    if ch.upper()!=x and ch.lower()!=x:
      str2+=ch
    print('result:%s'%str2)