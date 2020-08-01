firstnumber = input("Enter a number: ")
secondnumber = input("Enter second number: ")
print("\n\nFirst Number: " + str(firstnumber))
print("Second Number: " + str(secondnumber))

if firstnumber==secondnumber:
    print("\n\nBoth numbers are equal")
elif firstnumber>secondnumber:
    print("\n\nFirst number is greater than second number")
else:
    print("\n\nSecond number is greater than first number")