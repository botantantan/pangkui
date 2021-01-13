"""
Input sample:
[4,7,5,6,8,6,9,5]
Sample output:
4 7 5 6 8 9
Test data: sample samples are equivalent; list elements are equal; list elements have multiple consecutive repetitions
"""

lst1 = eval(input()) # mengindikasikan itu sebagai list
lst2 = list(set(lst1))
lst2.sort(key = lst1.index)
print(' '.join(list(map(str, lst2))))