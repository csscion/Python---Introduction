info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003} 
print(info['name'])  
print(info.get('eligible'))  

print(info.values())  
print(info.keys())  
print(info.items()) 
# print(info['name3'])  

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003} 
info.popitem() 
print(info) 

# del info['age'] 
# print(info) 
# del info 
# print(info) 


info = {'name':'Karan', 'age':19, 'eligible':True} 
info.pop('name') 
print(info) 

info = {'name':'Karan', 'age':19, 'eligible':True} 
print(info) 
info.update({'age':20}) 
info.update({'DOB':2001}) 
print(info) 