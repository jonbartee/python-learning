import time

def times_table():
    while True:
        try:
            x = int(input("Please enter range for times table: "))
            print()
            print(f'{"Times Table":^{(x+1)*4}s}')
            print(f'{"="*(x+1)*4}')
            for row in range(x+1):
                for col in range(x+1):
                    if row == 0:
                        print(f"{col:4}", end="")
                    elif col == 0:
                        print(f"{row:4}", end="")
                    else:
                        print(f"{row*col:4}", end="")
                print()
        except ValueError:
            print("Oops, please enter a number.")
            time.sleep(2)
        print()
        q = input("Do you want another table? y/n ").lower()
        if q[0] == "n":
            break

times_table()