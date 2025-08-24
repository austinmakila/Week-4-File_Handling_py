#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
    

# Step 1: Read the original file
with open("input.txt", 'r') as file:
        data = file.read()


    # Step 2: Modify the content (example: convert to uppercase)
modified_data = data.upper()

    # Step 3: Write the modified content to a new file
with open("output_Modified.txt", 'w') as file:
    file.write(modified_data)
print("File processed successfully. Modified content written to output_output.txt")




## Error Handling Lab: Read file with user input and handle errors
filename = input("Enter the filename you want to read (with extension please): ")

try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        content = file.read()
    print("\n File content:\n")
    print(content)
    print(f"File {filename} successfully loaded")

except FileNotFoundError:
    print(f" Error: The file '{filename}' does not exist or incorrect extension.")
