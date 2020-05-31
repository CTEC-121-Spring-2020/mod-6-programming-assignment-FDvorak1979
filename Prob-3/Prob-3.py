# Module 7
#   Programming Assignment 10
#     Prob-3.py

# <YOUR NAME>

def main():
    # your code here

    # do not change the while loop definition below
    total = 0.0
    count = 0
    x = float(input("Enter a number (Negative to quit) >> "))
    while x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Enter a number (negative to quite) >> "))
    print("\nThe average of the numbers is", total / count)
    
    while True:
        number = float(input("Enter a positive number: "))
        if number >= 0:
            break # Exit loop if number is valid.
        else:
            print("The number you entered was not positive")

main()    