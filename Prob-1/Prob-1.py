# Module 7
#   Programming Assignment 10
#     Prob-1.py

# Frank Dvorak

def main():
    total = 0.0
    count = 0
    x = float(input("Enter a number (Negative to quit) >> "))
    while x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Enter a number (negative to quite) >> "))
    print("\nThe average of the numbers is", total / count)

main()    