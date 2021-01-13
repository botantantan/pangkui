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

a = eval(input()) # terima input dictionary 1
b = eval(input()) # terima input dictionary 2
s = [] # semacam tempat simpen sementara

for i in a : # loop dictionary 1
  for j in b : # loop dictionary 2
    if i == j : # kalo key di dict 1 sama dengan key di dict 2
      a[i] = a[i] + b[j] # tambahin value yang punya key tersebut di dict 1
      s.append(i) # masukin key yang punya kembaran ke list s

for k in range(0,len(s)) : # loop sebanyak panjang s
  del b[s[k]] # delete item di dictionary 2 yang punya key kembaran di dictionary 1

# dictionary 2 udah gk ada key yg kembar sama dictionary 1

a.update(b) # masukin item sisa nya
c = sorted(a.items(), reverse=True) # list c yang nilai item dari dict 1 yang udh diurut menurun

print("{", end="")
for i in range(len(c)):
  if (type(c[0][0]) == int): # list of lists
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