file_name= 'Python/login_data_file.txt'

#read file data
with open (file_name, "r") as file:
    filedata= file.read()
print("file data read:\n",filedata)

with open (file_name, "r") as file:
    filedata= file.readline(15)
print("file data readline:\n",filedata)

with open (file_name, "r") as file:
    filedata= file.readline()
print("file data readline:\n",filedata)

with open (file_name, "r") as file:
    filedata= file.readlines()
print("file data readlines i.e. LIST:\n",filedata)

with open (file_name, "r") as file:
    filedata= file.readable()
print("file data readable:\n",filedata)

