
# ------------if else----------------
a = int(input("Enter your age: ")) 
print("Your age is:", a) 

# Conditional operators  
# >, <, >=, <=, ==, != 
# print(a>18) 
# print(a<=18) 
# print(a==18) 
# print(a!=18) 

if(a>18): 
  print("You can drive") 
  print("Yes") 
else: 
  print("You cannot drive") 
  print("No") 
  print("Yay!") 

# -------------elif---------------



num = int(input("enter a number")) 

if (num < 0):
    print("Number is negative.") 
elif (num == 0): 
    print("Number is Zero.") 
else: 
    print("Number is positive.")
# ---------------nested------------- 
num = 18 
if (num < 0): 
    print("Number is negative.") 
elif (num > 0): 
    if (num <= 10): 
        print("Number is between 1-10") 
    elif (num > 10 and num <= 20): 
        print("Number is between 11-20") 
    else: 
        print("Number is greater than 20") 
else: 
    print("Number is zero") 
# --------------match case-------------- 
x = int(input("Enter the value of x: ")) 
# x is the variable to match 

match x: 
    # if x is 0 
    case 0: 
        print("x is zero") 
    # case with if-condition 
    case 4: 
        print("case is 4") 
    case _ if x!=90: 
        print(x, "is not 90") 
    case _ if x!=80: 
        print(x, "is not 80") 
    case _: 
        print(x)
 # ----------------------------
#  