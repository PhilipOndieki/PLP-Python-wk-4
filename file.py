# Combined File Read & Write Challenge with Error Handling

# Ask user for filename
filename = input("Enter the filename to read: ")

# Try to read the file with error handling
try:
    with open(filename, "r") as file:
        content = file.read()
        print("\nFile contents:")
        print(content)
        print("\n")
    
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
    with open("output.txt", "w") as file:
        file.write(f"WORD COUNT: {number_of_words}\n\n")
        file.write(uppercase)

    # Print a success message once the new file is created
    print("SUCCESS: output.txt has been created with the processed text and word count!")
        
except FileNotFoundError:
    print(f"ERROR: File '{filename}' not found!")
    
except PermissionError:
    print(f"ERROR: Permission denied to read '{filename}'!")
    
except Exception as e:
    print(f"ERROR: Something went wrong: {e}")