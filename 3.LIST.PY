my_list = [1, 2, 3]
original_id = id(my_list)
print(f"Original ID: {original_id}")
# Modify the list
my_list.append(4)
# Check if the ID is the same after modification
modified_id = id(my_list)
print(f"modified ID: {original_id}")



details = ["Abhijeet", 18, "FYBScIT", 9.8,(1.52)] 
print(details) 
print(len(details))
print(type(details)) 

print(details[4:]) 
print(details[1:4]) 
print(details[-2:]) 
print(details[::-1]) 

print(details+ ['new item'])
print(details)

print(details*2)


num = [4,2,5,3,6,1,2,1,2,8,9,7] 
print(num) 
num.sort() 
print(num) 
num.sort(reverse=True) 
print(num) 

num = [4,2,5,3,6,1,2,1,2,8,9,7] 
print(num) 
num.reverse() 
print(num) 

num = [4,2,5,3,6,1,2,1,2,8,9,7] 
print("first occurance of 1 is at position",num.index(1)) 

num = [4,2,5,3,6,1,2,1,2,8,9,7] 
print("1 appears for",num.count(1),"times.") 

num = [4,2,5,3,6,1,2,1,2,8,9,7] 
print(num) 
print("adding 1 to ending",num.append(1)) 
print(num) 


num = [4,2,5,3,6,1,2,1,2,8,9,7] 
print(num) 
print("adding 1 to ending",num.insert(1,"Suraj")) 
print(num) 

num = [4,2,5,3,6,1,2,1,2,8,9,7] 
colors = ["voilet", "indigo", "blue"] 
print(num) 
print(colors) 
num.extend(colors) 
print(num) 

num = [4,2,5,3,6,1,2,1,2,8,9,7] 
colors = ["voilet", "indigo", "blue"] 
print(colors+num) 

countries = ["Spain", "Italy", "India", "England", "Germany"] 
print(countries) 
countries.clear() 
print(countries) 

countries = ["Spain", "Italy", "India", "England", "Germany"] 
print(countries) 
countries.pop(2) 
print(countries) 

countries = ["Spain", "Italy", "India", "England", "Germany"] 
print(countries) 
countries.remove("Spain") 
print(countries) 



lst= [s for s in range(6) ] 
print(lst) 
Suraj=(1,2,3,4,5,6) 
nw=[a for a in Suraj] 
print(nw) 
ds=[b for b in Suraj if b%2==0] 
print(ds) 

lst=[0,1,2] 
print(lst.pop())