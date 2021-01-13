"""
Input example 1:
{1:3,2:5}
{1:5,3:7}
Output sample 1:
{3:7,2:5,1:8}
Input example 2:
{'c':3,'a':4,'n':1}
{'a':3,'c':7,'b':10}
Output sample 2:
{'n':1,'c':10,'b':10,'a':7}
"""

a=eval(input())
b=eval(input())
s=[]
for i in a :
    for j in b :
        if i==j : a[i]+=b[j]
        if i == j: s.append(j)
for k in range(0,len(s)) :
    del b[s[k]]
a.update(b)
c=sorted(a.items(), reverse=True)

print("{", end="")
for i in range(len(c)):
  if (type(c[0][0]) == int):
    if (i == len(c)-1):
      print("{}:{}".format(c[i][0], c[i][1]), end="")
    else:
      print("{}:{},".format(c[i][0], c[i][1]), end="")
  else:
    if (i == len(c)-1):
      print("'{}':{}".format(c[i][0], c[i][1]), end="")
    else:
      print("'{}':{},".format(c[i][0], c[i][1]), end="")
print("}")