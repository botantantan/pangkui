"""
Input sample:
+-P-xf4+-1!#
Sample output:
-3905
"""

def filterFunc1(s):
  if (s=="-" or s=="x" or s=="0" or s=="1" or s=="2" or s=="3" or s=="4" or s=="5" or s=="6" or s=="7" or s=="8" or s=="9" or s=="a" or s=="b" or s=="c" or s=="d" or s=="e" or s=="f" or s=="A" or s=="B" or s=="C" or s=="D" or s=="E" or s=="F"):
    return True
  else:
    return False

def filterFunc2(s):
  if (s=="-" or s=="x"):
    return False
  else:
    return True

s_in = input() # +-P-xf4+-1!#

s_temp = ""
s_out = ""
flag = False

s_fil1 = filter(filterFunc1, s_in) # {-, -, x, f, 4, -, 1}
for c in s_fil1:
  s_temp = s_temp + c # --xf4-1

if (s_temp[0] == "-"):
  flag = True # True negatif, False positif

s_fil2 = filter(filterFunc2, s_temp) # {f, 4, 1}
for c in s_fil2:
  s_out += c # f41

if (s_out == ""):
  print("0")
else:
  if (flag == True):
    print(int(s_out, 16)*-1)
  else:
    print(int(s_out, 16))