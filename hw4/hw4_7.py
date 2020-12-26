"""
Input sample:
red yellow blue green white
Sample output:
After sorted:
blue
green
red
white
yellow
"""

s = input()

s = s.split()
s.sort()
print("After sorted:")
for word in s:
  print(word)