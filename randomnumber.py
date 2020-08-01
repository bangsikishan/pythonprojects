import random
inputnumber = int(input("Enter a number between 1 to 5: "))
randomnumber = random.randint(1,10)
if inputnumber==randomnumber:
    print("\nNumber Matched!")
else:
    print("\nNo Matches!")
print("\nYour number: " + str(inputnumber))
print("Computer number: " + str(randomnumber))