# File Read & Write Challenge 🖋️:
#  Create a program that reads a file and writes a modified version to a new file.

# Read the contents of input.txt
file = open("input.txt", "r")
content = file.read()
print("File contents:")
print(content)
print("\n")
file.close()

# Count the number of words in the file
words = content.split()
number_of_words = len(words)
print(f"Number of words: {number_of_words}")
print("\n")

# Convert all text to uppercase
uppercase = content.upper()
print("Uppercase content:")
print(uppercase)
print("\n")

# Write the processed text and the word count to a new file called output.txt
file = open("output.txt", "w")
file.write(f"WORD COUNT: {number_of_words}\n\n")
file.write(uppercase)
file.close()

# Print a success message once the new file is created
print("SUCCESS: output.txt has been created with the processed text and word count!")