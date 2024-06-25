# Create two variables, str1 and str2

# Define str1
str1 = "Hello, "
# Define str2
str2 = "World"

# Concatenate str1 and str2
concat_result = str1 + str2

# Repeat str1 3 times
repetition_result = str1 * 3

# Print the values of all the variables
print("str1: ", str1)
print("str2: ", str2)
print("concat_result: ", concat_result)
print("repetition_result: ", repetition_result)

# Print the first character of str1
print("The first character of str1 is: ", str1[0])

# Printing our the last character of str2
print("The last character of str2 is: ", str2[4])

# Printing out the substring from 2nd to 5th character to console
print("The substring of str1 from the 2nd to the 5th character is: ", str1[1:5])

# Add a line separator
print("\n")


# Print a grid of 3x3 with "O" in each cell
for _ in range(3):
    print("O O O")



# Add a line separator
print("\n")



# Print a 2x4 grid with * and a hollow middle
# Print the top row of *'s
print("****")

# Print the middle hollow row
print("    ")

# Print the bottom row of *'s
print("****")

# Add a line separator
print("\n")

# Print a 4x6 grid with X and a hollow middle
# Print the top row of X's
print("X" * 6)

# Print the middle hollow rows
for _ in range(2):
    print("X" + " " * 4 + "X")

# Print the bottom row of X's
print("X" * 6)


