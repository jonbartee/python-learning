import time
import random

# def times_table():
#     while True:
#         try:
#             x = int(input("Please enter range for times table: "))
#             print()
#             print(f'{"Times Table":^{(x+1)*4}s}')
#             print(f'{"="*(x+1)*4}')
#             for row in range(x+1):
#                 for col in range(x+1):
#                     if row == 0:
#                         print(f"{col:4}", end="")
#                     elif col == 0:
#                         print(f"{row:4}", end="")
#                     else:
#                         print(f"{row*col:4}", end="")
#                 print()
#         except ValueError:
#             print("Oops, please enter a number.")
#             time.sleep(2)
#         print()
#         q = input("Do you want another table? y/n ").lower()
#         if q[0] == "n":
#             break
##END FUNCTION

# times_table()


##prime numbers 

##Taking input(not working)
# def prime():
#     x = int(input("Enter a number to check if it's prime: "))

#     for i in range(2,x):
#         if x%i == 0:
#             print()
#             print(x, "is not a prime number.")
#             print()
#             break
#     print(x, "is a prime number!")
##END FUNCTION

# prime()

##or

##Iterating a list(working)
# def isprime(x):
#     for i in range(2,x):
#         if x%i == 0:
#             return False
#     return True
##END FUNCTION

# testprime = [3,10,11,31,44,65,99,109]

# for x in testprime:
#     print(f"{x} is a prime number {isprime(x)}")

## Counting prime numbers

# def nth_prime(x):
#     num = 3
#     prime = 2
#     if x == 1:
#         return 2
#     while prime < x:
#         num += 2
#         if isprime(num):
#             prime += 1
#     return num
##END FUNCTION

# primes = [i for i in range(2,101) if isprime(i)]

# print(primes)

## Guessing game
# def guessing_game():    
#     while True:
#         answer = random.randint(1,20)
#         print(answer)
#         guess = int(input("Please guess a number between 1 and 20: "))
#         try:
#             print()
#             while guess != answer:
#                 if guess < 1 or guess > 20:
#                     guess = int(input("Please guess a number between 1 and 20: "))
#                     print()
#                 else:
#                     print("That's not it! Guess again!")
#                     print()
#                     guess = int(input("Please guess a number between 1 and 20: "))
#                     print()
#             else:
#                 print("That's it! You Win!")
#                 print()
#         except ValueError:
#             print("Oops please enter a number.")

#         q = input("Do you want to play again? y/n ").lower()

#         if q[0] == "n":
#             break
# ##END FUNCTION

# guessing_game()

## Leap year checker

# def isLeapYear(x):
#     if x % 4 == 0:
#         if x % 100 == 0:
#             if x % 400 == 0:
#                 return True
#             else: return False
#         else: return False
#     else: return False
# ## END FUNCTION

# years = [1992, 1600, 1900, 2000, 2002, 2020]

# for year in years:
#     x = isLeapYear(year)
#     if x == True:
#         print(year, "is a leap year!")
#     else:
#         print(year, "is not a leap year.")


##Enumerate function
names = ['Sam', 'Tom', 'Steve']

for name in range(len(names)):
    print(name+1, names[name])

print()

new = enumerate(names)
new = list(new)
print(new)

print()

for i in enumerate(names, start=1):
    print(i) 

for num, name in enumerate(names, start=1):
    print(num, name)