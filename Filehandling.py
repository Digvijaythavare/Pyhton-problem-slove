File_name = input("Enter the file name:")

try:
    with open(File_name, 'r') as json_file:
        json_file.read()

except FileNotFoundError:
    with open(File_name, 'w') as json_file:
        json_file.write("File handling example.")
        json_file.read()
        json_file.close()

else:
    print("File already exists. Please choose a differenr name ")