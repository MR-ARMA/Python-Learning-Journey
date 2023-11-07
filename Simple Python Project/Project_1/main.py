import re


with open('file_1.txt', 'r') as file:
    file_1 = file.read()

with open('file_2.txt', 'r') as file:
    file_2 = file.read()
    
list_ = re.findall('[0-9]+', file_1)
print(sum(int(num) for num in list_))

list_ = re.findall('[0-9]+', file_2)
print(sum(int(num) for num in list_))