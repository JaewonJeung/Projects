import os
from datetime import datetime
import re

#get current working directory
print(os.getcwd())

#forward slash instead of backslash
os.chdir('C:/Users/jeawu/AppData')
print(os.getcwd())

#ls. directory params inside listdir()
print(os.listdir())

#creating multiple directories using one function. Cannot create dirs when it already exist
#os.mkdir('PythonTestDir')
os.makedirs('PythonTestDir/Subdir1')  #able to create multiple directories
print(os.listdir())

#removing directories
#os.rmdir('PythonTestDir/Subdir1')
os.removedirs('PythonTestDir/Subdir1')  #able to delete multiple directories
print(os.listdir())

#rename file/folder
os.mkdir('test_folder')
os.rename('test_folder', 'renamed_folder')  #from, to
print(os.listdir())
os.rmdir('renamed_folder')

#info check
os.mkdir('testfolder')
print(os.stat('testfolder'))  #.st_size to check file size
mod_time = os.stat('testfolder').st_mtime  #modified time
print(datetime.fromtimestamp(mod_time))  #checking modtime in a human-readable format
os.rmdir('testfolder')

#directories. os.walk yields tuples.
for dirpath, dirnames, filenames in os.walk('C:/Users/jeawu/OneDrive/Documents'):  #goes through the entire tree
    print('current path: ', dirpath)
    print('directory names: ', dirnames)
    print('filenames: ', filenames)
    print()
    if 'Arrow' in dirnames:
        break
print(os.path.exists('/fakepath/shouldReturnFalse'))
print(os.path.basename('/fakepath/shouldReturnFalse'))
print(os.path.dirname('/fakepath/shouldReturnFalse'))
print(os.path.split('/fakepath/shouldReturnFalse'))
#more .path methods
print(os.path.isdir('C:/Users/jeawu/OneDrive/Documents'))
print(os.path.isfile('C:/Users/jeawu/OneDrive/Documents'))
print(os.path.splitext('/fakepath/shouldReturnFalse.txt'))  #splits the extension from the file name

#environment variable
print(os.environ)  #traditionally, 'set' on cmd
print(os.environ.get('USERPROFILE'))  #HOME for Mac

# joining paths together
file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')  #accepts multiple arguments
print(file_path)

#--------------------- automating file name changes
print('--------------------- automating file name changes')
os.chdir('C:/Users/jeawu/OneDrive/Documents/PythonScripts')
for file in os.listdir():
    file_name, file_ext = os.path.splitext(file)  #splitting extension
    try:
        file_title, file_copy, file_number = re.split(' - | ', file_name)  #filename.split but re built-in does accepts multiple delimiters
    except Exception:
        print('some files do not match the convention:', file_name)
        if (file_name == 'testfile - Copy'):
            file_title, file_copy, file_number = 'testfile', 'Copy', '(1)'
        else:
            file_title, file_copy, file_number = 'testfile', 'Copy', '(0)'
    file_number = file_number.replace('(', '')
    file_number = file_number.replace(')', '').zfill(2)  #filling in leading 0s

    new_name = ('{}-{}{}'.format(file_number, file_title, file_ext))
    os.rename(file, new_name)  #renaming a file
    