# ------------for---------
name = 'Abhishek' 
for i in name: 
    print(i, end=", ") 

colors = ["Red", "Green", "Blue", "Yellow"] 
for x in colors: 
    print(x) 

for k in range(5): 
    print(k) 

for k in range(4,29,5): 
    print(k) 
# ------------While ---------
count = 5 
while (count > 0): 
  print(count) 
  count = count - 1 

x = 5 
while (x > 0): 
    print(x) 
    x = x - 1 
else: 
    print('counter is 0') 
# ------------do While ---------
while True: 
  number = int(input("Enter a positive number: ")) 
  print(number) 
  if  number < -1: 
    break 
# ------------Break  ---------
for i in range (5): 
    print(i) 
    if i==2: 
        break 

# ------------Continue ---------
for i in range (5): 
    if i==2: 
        continue 
    print(i) 
# --------pass------------
for i in "Suraj":
    if i=='u':
        pass
        print("this is pass block")
    print(i)
# --------------------
for x in range(5): 
    print ("iteration no {} in for loop".format(x+1)) 
else: 
    print ("else block in loop") 
print ("Out of loop") 
# ------------Short hand if else:  ---------

a = 2 
b = 330 
print("A") if a > b else print("B") 
# ------------ ---------