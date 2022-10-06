
# Working with files in python part 1: Opening and reading files 
# In this lesson we will learn how to open existing files, read content in the files and close files
# we will also learn how to properly display the content in a file using loops
# we will also implement the use of functions and also the try: except: blocks for error detection.
# written by Mahmud Shuaib 
# 4th October 2022  

def BasicReading():
    superfile = open('superfile.txt' , 'r')  
    print(superfile.read())
    superfile.close()
# calling the file 
#BasicReading() 

def ReadingFilesError():
    try:
        our_file = open("sample")
    except FileNotFoundError as file_error:
        print("File does not currently exist, Error Message: ",file_error)
#calling the method
#ReadingFilesError()

def ReadingExistingFile():
    # lets open an existing file 
    try:    
        existing_file = open('superfile.txt','r') # flag r means 'read content in the file'
        print(existing_file.read()) # read the content of the file using the read method 
    except FileNotFoundError as file_error:
        print("File does not currently exist, Error Message: ",file_error)
    finally:
        existing_file.close()
        print('File Closed')
# calling the method
#ReadingExistingFile()

# reading the file from a path 
#file_r = open(r"C:\Users\Mahmus\Dropbox\PC\Desktop\Pythonprogramming\superfile.txt", 'r')
# without the use of the raw string r you can use double escape strokes
file_r = open("C:\\Users\\Mahmus\\Dropbox\PC\\Desktop\\Pythonprogramming\\superfile.txt", 'r')
#print(file_r.read())
# the read method accepts arguments 
# we can read the first few characters in a text by passing a number 
#print(file_r.read(10)) # prints the first 10 characters 

# read a single line of a file 
# chain readlines to read multiple lines 
print(f'line 1: {file_r.readline()}')
print(f'line 2: {file_r.readline()}')
print(f'line 3: {file_r.readline()}')
file_r.close() # closing the file here

# looping through the file
# we need to open the file again 
file_r = open("C:\\Users\\Mahmus\\Dropbox\PC\\Desktop\\Pythonprogramming\\superfile.txt", 'r')
print('***********file Looping*****************') 
for content in file_r:
    print(content, end = "")
# close the file    
file_r.close()












 





    
