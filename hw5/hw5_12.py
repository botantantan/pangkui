"""
Input sample:
Here is a set of inputs. E.g:
1234 608
Sample output:
The corresponding output is given here. E.g:
44
"""

a,b=map(int,input().split())
a=abs(a)
b=abs(b)
sum=0
while True:
    if a==0 and b==0:
        break
    sum=sum+((a%10)*(b%10))
    a=a//10
    b=b//10
print(sum)