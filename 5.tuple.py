countries = ("Spain", "Italy", "India", "England", "Germany") 
print(countries) 
temp = list(countries) 
temp.append("Russia")       #add item  
temp.pop(3)                 #remove item 
temp[2] = "Finland"         #change item 
countries = tuple(temp) 
print(countries) 