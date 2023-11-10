# ==============strings===========
s = 'Hello World'
print(s)
print('length of the string is',len(s), 'characters')
print(s[0])
print(s[0:4])
print(s[-4:])
print(s[0:9:2])
print(s[::-1])
print(s[::-2])
print(s + ' concatenate me!')

letter = 'z'
print(letter*10)


a="hi !!!My name is Suraj !!!!"  
print(a)  
print(a,"Length is",len(a))  
print(a.upper())  
print(a.lower())  
print(a.replace("Suraj","Scion")) 
print(a.capitalize())  
print(a.title())  
print(a.swapcase())  
print(a.find("M"))  
print(a.find("x")) 
print(a.index("M"))  

#print(a.index("x"))  #uncomment to see the exception 

print(a.count("i"))  
print(a.strip("!"))  
print(a.rstrip("!"))  
print(a.split(" "))  
print(a.center(50,"-"))  
print(a.endswith("!"))  
print(a.endswith("a",4,10))  
print(a.endswith("n",4,10))    
print(a.isalnum())  
print(a.isalpha())  
print(a.islower())  
print(a.isprintable())  
print(a.isspace())  
print(a.istitle())  
print(a.isupper())  
print(a.startswith("!"))  



letter = "Hey my name is {1} and I am from {0}" 
country = "India" 
name = "Harry" 
print(letter.format(country, name)) 
print(f"Hey my name is {name} and I am from {country}") 
print(f"We use f-strings like this: Hey my name is {{name}} and I am from {{country}}") 
price = 49.09999 
txt = f"For only {price:.2f} dollars!" 
print(txt) 
# print(txt.format()) 
print(type(f"{2 * 30}")) 


