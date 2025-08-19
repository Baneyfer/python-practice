# file_path = (r'data.csv')
# print(file_path)

# # absolute path 
# # c://computer/users/baney/documents/data.csv

# # relative path
# # data.csv <-- in relation to where we're at like in html (calling to known file)

# #write to a file 
# f = open("samplefile.txt", "w") 

# #close a file
# f.close()
# import os

# f = open('sampledata.txt')
# #f.write("Hello") #<--- overwrites the data in the open file, running this created the file

# sample_lines = f.readlines()
# f.close()
# print(sample_lines)

# for line in sample_lines:
#     print(line)

# os.remove('sampledata.txt')

from_user = input("Type Something: ")

f = open('samplefile.txt', 'a')
f.write(from_user + '\n')
f.close