# creating the algorithm
# showing the heading
print("Welcome to Alphabeter where you can identify a alphabet")

# showing the rules
print("Type only one character not more than the program may get malfunctioned.")

# getting the input from the user
given = str(input("Enter a string: "))

# checking the input
if (given >= "a" and given <= "z") or (given >= "A" and given <= "Z"):
    print(given, "is a alphabet.")

# making the else condition

else:
    print(given, "is not a alphabet.")

print("Process Done!")