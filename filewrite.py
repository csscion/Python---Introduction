file_name= 'Python/filewrite.txt'


#read file data
with open (file_name, "r") as file:
    filedata= file.read()
print("file data read:\n",filedata)

#rewrite entire file data
with open (file_name, "w") as file:
    file.write("W is used to add new data , however previous data gets removed")

#read new file data
with open (file_name, "r") as file:
    filedata= file.read()
print("file data after using write mode is:\n",filedata)

# add new data to existing data
with open(file_name,"a")as file:
    file.write("\nThis data is added without deleting prev data")

with open (file_name, "r") as file:
    filedata= file.read()

print("file data after using append mode is:\n",filedata)

with open(file_name, "r") as file:
    position = file.tell()
    print("Current file position:", position)

with open(file_name, "r") as file:
    # Move the file pointer to byte offset 10
    file.seek(10)
    data = file.read()
    
    print("Data from byte offset 10:", data)
    position = file.tell()
    print("Current file position:", position)

