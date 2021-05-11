'''
This python program will take two files of dehydrated tweets and merge them. To
use this program, download it from Github and store it in your twarc utilities
file.

Usage: python utils/combine.py

Takes user input of the following:
file1 - 
file2 -
output - 

Each id must be on a separate line in the original tweet file for this to work. The program reads line by line. 
'''
file1 = input("Enter the name of your filter txt: ")
file2 = input("Enter the name of your search txt: ")
output = input("Enter the name of your output txt: ")


filenames = [file1, file2]
  
# Open file3 in write mode
with open(output, 'w') as outfile:
  
    # Iterate through list
    for names in filenames:
  
        # Open each file in read mode
        with open(names) as infile:
  
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())
  
        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")
