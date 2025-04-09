#File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified 
# version to a new file.

with open('input.txt', 'r') as file:
    data = file.read()
    changes_made = data.replace('old_content', 'new_content')# replace with actual content
    with open('output.txt', 'w') as file: # open in write mode to save changes
        file.write(changes_made)
        print("File modified successfully.")

    
#Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t 
# exist or can’t be read.
filename = input("Enter the name of you file: ")
try:
    with open(filename, 'r') as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print(f"Error: The requested file '{filename}' does not exist.")
finally:
    print("Execution completed.")
