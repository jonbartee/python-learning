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

# prime()

##or

##Iterating a list(working)
# def isprime(x):
#     for i in range(2,x):
#         if x%i == 0:
#             return False
#     return True

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

# primes = [i for i in range(2,101) if isprime(i)]

# print(primes)

def guessing_game():
    answer = random.randint(1,101)

    while True:
        try:
            pass
            guess = int(input("Please guess a number between 1 and 100: "))
            print()

        except ValueError:
            print("Oops please enter a number.")
            