
from functools import reduce 


def name(fname, lname): 
    print("Hello,", fname, lname) 
name("Sam", "Wilson")
name("Suraj", "Damgude")

def calgm(a,b): 
    mean=(a*b)/(a+b) 
    print(mean) 

def isgreaterthan(a,b): 
    if a<b: 
        print("Second is bigger") 
    else: 
        print("First is bigger") 

a=5 
b=6 
c=4 
calgm(a,b) 
isgreaterthan(a,b) 
calgm(b,c) 
isgreaterthan(b,c) 
calgm(a,c) 
isgreaterthan(a,c) 


def funct(): 
    return 1,2,3,4 

tup= funct() 
a,b,c,d= funct() 
print(tup) 
print(a) 


def name(fname, mname = "Tukaram", lname = "Damgude"): 
    print("Hello,", fname, mname, lname) 
name("Suraj") 
name("Suraj","T","D") 
# =============default=================
def name(fname, mname = "Tukaram", lname = "Damgude"): 
    print("Hello,", fname, mname, lname) 

name("Suraj") 
name("Suraj","T","D") 

# ================keyword==============
def name(fname, mname, lname): 
    print("Hello,", fname, mname, lname) 
name(mname = "Tukaram", lname = "Damgude", fname = "Suraj") 
name(lname = "Damgude", mname = "Tukaram", fname = "Suraj") 
# ==============================

def name(fname, mname, lname): 
    print("Hello,", fname, mname, lname) 
name("Tukaram",   "Damgude",  "Suraj") 
name( "Damgude",  "Tukaram",  "Suraj") 


# ==============================
def arbitrary_arguments(*args):
    for arg in args:
        print(arg)

arbitrary_arguments(1, 2, 3, 4)
# ---------------------


def avg(*numbers): 
    print(type(numbers)) 
    sum=0 
    for i in numbers: 
        sum=sum+i 
    print("average is",sum/len(numbers))
avg(12.4854,54,58,56) 
# ------------------

def add_all_nums(*args):    
    print(args) 
    print(*args)
    print(sum(args)) 
add_all_nums(1,2,3,4,5,6,7,8,9)
numbers = (1,2,3,4,5,6,7,8,9)
add_all_nums(*numbers)
numbers_list = [1,2,3,4,5,6,7,8]
add_all_nums(*numbers_list)
# # ==============================



# # ==============================
def name(**name): 
    print(type(name)) 
    print("Hello,", name["fname"], name["mname"], name["lname"]) 
name(mname = "Tukaram", lname = "Damgude", fname = "Suraj") 
# # ==============================


def keys_and_values(**kwargs):              
    print(kwargs) 
    print(*kwargs)      
    for value, key in kwargs.items():    
        print(key, value)
keys_and_values(name="Harsh", last_name="Dusane", occupation="Tech Trainer")

# # =============lambda=================
squarefunc = lambda x: x*x 
squarefunc(3) 
print(squarefunc(3)) 

add = lambda x,y:x+y
add(3,4)
print(add(3,4))

# # ==============map================
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
Squared_list = list(map(lambda x : x*x, elements)) 
print(Squared_list) 

# # =============Filter=================
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
New_list = list(filter(lambda x : (x%2 !=0), elements)) 
print(New_list) 

# # =================reduce=============

elements = [1, 2, 3, 4, 5] 
result1 = reduce(lambda x, y : x + y, elements) 
result2 = reduce(lambda x, y : x * y, elements) 
print(result1, result2) 

# # =================Enumerate=============

fruits = ['apple', 'banana', 'mango'] 
for index, fruit in enumerate(fruits): 
    print(index, fruit) 

fruits = ['apple', 'banana', 'mango'] 
for index, fruit in enumerate(fruits, start=1): 
    print(index, fruit) 

fruits = ['apple', 'banana', 'mango'] 
for index, fruit in enumerate(fruits): 
    print(f'{index+100}: {fruit}')