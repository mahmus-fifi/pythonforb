"""
# program to read and write a file 
new_file = open('doc.txt','w')
new_file.write('This is a line of text in the doc file')
# opening the file in read mode 
new_file = open('doc.txt', 'r')
read_file = new_file.read()
print(f'Content in the doc.txt file: {read_file}')
new_file.close()
"""

def WritingToAFile():
    try:
        file_write = open('superfile.txt', 'a')
        file_write.write('I am a new line of text')
    except FileExistsError:
        print('Cant find the file here')
    finally:
        print('Finally section: write action executed')
        
    try:
        file_write = open('superfile.txt', 'r')
        print(file_write.read())
    except FileNotFoundError:
        print('file not found!')
    finally:
        file_write.close()
#WritingToAFile()

# we have the 'a' appends , 'r' read, 'w' write, 'x' create 
# creating a file 
def CreateFile():
    try:
        new_file = open('freshfile.txt','x')
        new_file.close()
    except (FileExistsError, UnboundLocalError):
        print('file already exists')
    finally:
        print('code completed') 
# run the method
CreateFile() 


        

