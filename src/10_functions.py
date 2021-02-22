# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(nums):
    if(nums % 2 == 0):
        print("even")
        return True
    else:
        print("odd")

is_even(2)
is_even(3)
is_even(4)
is_even(5)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
is_even(num)

