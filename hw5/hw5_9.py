"""
Input example 1:
FONTNAME and FILENAME
Output sample 1:
FONTAMEIL
Input example 2:
fontname and filrname
Output sample 2:
Not Found
"""

str1 = input()
str2 = ''    
str3 = ''    
for ch in str1:
    if ord('A') <= ord(ch) <= ord('Z'):
        str2 += ch
mylist = list(set(str2))       
                               
mylist.sort(key = str2.index)  
for ch in mylist:              
    str3 += ch
if str3 != '':                 
    print(str3)
else:
    print("Not Found")

