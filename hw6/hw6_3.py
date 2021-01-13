"""
Input sample:
Here is a set of inputs. E.g:
  1,5,9,3,9,1,1,7,5,7,7,3,3,1,5,7,4,4,5,4,9,5,10,9
Sample output:
The corresponding output is given here. E.g:
6 8
"""

l=list(map(int,input().split(',')))
s=[i for i in range(6,11) if i not in l]
print(*s,sep=' ')


# versi pinteran dikit
l = input().split(",") # l masih string
for i in range(len(l)):  # ubah setiap item yang ada di l
  l[i] = int(l[i]) # l udah int

s = [i for i in range(6, 11) if i not in l]

print(*s, sep = " ")