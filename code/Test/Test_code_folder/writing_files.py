# lesson on writing files with python 
def WritingToAFile():
    try:
        file_write = open('superfile.txt','a')
        file_write.write('I am a new single line')
    except FileExistsError:
        print("Can't seem to find a file here")
    finally:
        print('file executed')
    try:
        file_write = open('superfile.txt', 'r')
        print(file_write.read())
    except FileNotFoundError:
        print('file not found')
    finally:
        file_write.close()
    
    #WritingToAFile()  # logical Error here         
WritingToAFile() 
# creating a file 
def CreateAFile():
    # we can use 'w' 'a' or 'x' to create the file 
    try:
        new_file = open('freshfile.txt', 'x')
        new_file.close()
    except (FileExistsError, UnboundLocalError):
        print('This file already exists')
    finally:
        print('code executed')

CreateAFile()
        
    