# file = open('test.txt', mode='x') # Create file mode
# file = open('test.txt', mode='w') # write file mode
# file = open('test.txt', mode='a') # append file mode
# file.write("\nHello everyone") 

file = open('test.txt') # read file mode
content = file.read()
file.close()
# count = 0
# for char in content:
#     if char == 'o':
#         count = count + 1


# print("Number of o is ", count)

import os

# list_of_files = os.listdir('C:\\Seed\\Python\\Lighthouse-Afternoon\\FileHandling')
# print(list_of_files)

# print("Already existed files and folders are ")
# for file in list_of_files:
#     print(file)

# os.mkdir("abc1")
# print("Directory created")

# os.rmdir('abc1')

# import shutil
# shutil.rmtree('abc1')
# print("Directory deleted...")

os.remove('test.txt')
print("File deleted..")