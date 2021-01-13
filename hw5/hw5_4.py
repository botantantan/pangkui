"""
Input sample:
ad2f3adjfeainzzzv
Sample output:
23adefijnvz
"""

s = input()

print("".join(sorted(set(s))))

str1=input()
str2=[]
for ch in str1:
  if ch not in str2:
    str2.append(ch)
str2.sort()
for ch in str2:
  print(ch,end='')
print()