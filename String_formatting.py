# # Given an integer, , print the following values for each integer 1 from n to :

# # Decimal
# # Octal
# # Hexadecimal (capitalized)
# # Binary

# # The four values must be printed on a single line in the order specified above for each  from  to .
# Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

# # Input Format
# # A single integer denoting .
def print_formatted(number):
    for i in range(1,n+1):
        space=len(bin(n)[2:])+1
        print(f"{str(i).rjust(space-1)}{str(oct(i))[2:].rjust(space)}{str(hex(i)).upper()[2:].rjust(space)}{str(bin(i))[2:].rjust(space)}")
    # your code goes here
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
