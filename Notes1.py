""" name = "Jon"

print(name)

for i in range(3):
    print(name)

for i in range(1,5):
    print(i)

testlist = list(range(5))
print(testlist)


#Defining functions
def hello():
    print("Hello")

hello()

def hello2():
    name = input("Enter name: ")
    print("Hello " + name)

#hello2()

#if statements

numbers = [1,5,2,4,6,10,3]
def oddoreven():
    for number in numbers:
        if number%2 == 0:
            print(number, "is even.")
        else:
            print(number, "is odd.")

oddoreven() """

#creating a table of numbers
for row in range(5):
 #   print(row)
    for col in range(5):
        print(col, end='')
    print()