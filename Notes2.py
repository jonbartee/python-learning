import random
#numbers = [random.randint(-20,20) for i in range(10)]

#print triangle of numbers

# for row in range(1,11):
#     for col in range(row):
#         print('{:3}'.format(col+1), end="")
#     print()


#using .format method
# def hello():
#     name = input("Enter name: ")
#     print("Hello {} nice to meet you.".format(name))

# hello()

#typecasting string to integer
# number = int(input("Enter Number: "))
# print(number)
# print(type(number))


#WHILE LOOPS
# count = int(input("Enter Number: "))
# print("Ready")
# while count >= 0: 
#     if count > 0:
#         print(count)
#     else:
#         print("BLASTOFF!!!")
#     count -= 1
    

#Append
# numbers = [1,-5,2,-4,0,6,-10,3]

# pos=[]
# neg=[]

# for i in numbers:
#     if i > 0:
#         pos.append(i)
#     else:
#         neg.append(i)

# print(pos)
# print(neg)


#List Comprehension
# numbers= [i for i in range(10)]
# print(numbers)

#pos = [i for i in numbers if i > 0]
#print(pos)

# list_numbers = []

# for i in range(5):
#     list_numbers.append(list(numbers))
# for i in list_numbers:
#     print(i)


#Shuffling numbers
#numbers = [i for i in range(1,26)]
#random.shuffle(numbers)
#print(numbers)

#horse race problem
shuffled = [10, 14, 25, 3, 23, 15, 18, 6, 4, 9, 20, 19, 5, 13, 17, 8, 12, 22, 2, 7, 1, 11, 16, 21, 24]
horses = [[],[],[],[],[]]

# for horse in shuffled:
#     print(horse)
# for race in horses:
#     print(race)

for i in range(5):
    for j in range(5):
        horses[j].append(shuffled.pop())

# for i in range(5):
#     print(horses[i])

# print()

for race in horses:
    race.sort()
    print(race)

def last(x):
    return x[-1]

sorted_horses = sorted(horses,key=last,reverse=True)

print()

for race in sorted_horses:
    print(race)