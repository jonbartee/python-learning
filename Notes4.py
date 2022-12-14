import math
import time
import random

# a = 'hi url nice to meet you'
# b = 'hi url its a nice day'
# c = 'hi url you look great'

# l = [a, b, c]

# for i in l:
#     n = str.split(i)[1]
#     print(n)

# s = 'Hi Jon nice to meet you'
# l = str.split(s)
# print(l)

# comma = 'Sam,Tom,Pete,Matt'

# new = comma.split(',')

# print(comma[0])
# print(new[0])

name = input("Please enter names separated by commas: ").split(',')
print(name)

names = [i.strip() for i in name]

print(names)

# names = str.split(names)
# print(names[0])