f = open(input("Give path for Ascii text: "), "r")
b=str(f.read())

binary_converted = ''.join(format(ord(c), '07b') for c in b)
#The join() method takes all items in an iterable and joins them into one string.
#The format() method formats the specified value(s) and insert them inside the string's placeholder. The format() method returns the formatted string.
#The ord() function returns the number representing the unicode code of a specified character.
print("ASCII Text: " + b)
print("\nThe Binary Representation is: ", binary_converted)

def maxConsecutiveDigit(num, d):
    count = 0
    max = 0
    for digit in num:
        if digit == d:
            count+=1
            if max < count:
                max = count
        else:
            count=0
    return max

print("\nMost consecutive 1s: " + str(maxConsecutiveDigit(binary_converted, '1')))
print("Most consecutive 0s: " + str(maxConsecutiveDigit(binary_converted, '0')))