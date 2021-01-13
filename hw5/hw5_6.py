"""
Input example 1:
Here is a set of inputs. E.g:
poemp134
Output sample 1:
The corresponding output is given here. E.g:
not found
Input example 2
Here is a set of inputs. E.g:
This is a test example
Output sample 2:
The corresponding output is given here. E.g:
Thisaexmpl
"""

string = input()
count = 0
result = ''
 
for i in string:
    if i.isalpha() and i.upper() not in result.upper():
        count += 1
        result += i     
 
if count >= 10:
    print(result[:10])
else:
    print('not found')