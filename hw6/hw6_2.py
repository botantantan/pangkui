"""
Input sample:
Here is a set of inputs. E.g:
4
{'a':{'b':10,'c':6}}
{'b':{'c':2,'d':7}}
{'c':{'d':10}}
{'d':{}}
Sample output:
The corresponding output is given here. E.g:
4 5 35
"""

n = int(input()) # input brp line
num = 0 # ada brp jalan (total edge)
sum = 0 # brp total panjang jalan (total dari nilai edge)

for i in range(n): # loop sebanyak n kali (total vertex) brp line
    dic = eval(input())
    for j in dic:
        temp = dic[j]
        for key in temp:
            num += 1
            sum += temp[key]

print("{:d} {:d} {:d}".format(n,num,sum))