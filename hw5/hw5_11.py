"""
Input sample:
a b c e f gh
Sample output:
ghfecba
['a','b','c','e','f','gh']
gh f e c b a
"""

str=input()
list=[]
for c in str.split():  
  list.append(c)	
print("".join(list[::-1]))	
print(list)					
print(" ".join(list[::-1]))	#lebih baik nama jangan pake yang ada lambang ijo