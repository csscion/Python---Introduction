a = (input("Enter an integer: ")) 
try:
    for i in range (1,11): 
        print(f"{int(a)} X {i} = {int(a)*i}") 
except : 
    print("iNVALID") 

print("ends") 
# ============================


def func1(): 
  try: 
    l = [1, 5, 6, 7] 
    i = int(input("Enter the index: ")) 
    print(l[i]) 
    return 2
  except: 
    print("Some error occurred") 
    return 0 
  finally: 
    print("I am always executed") 
  # print("I am always executed") 
x = func1() 
print(x) 


# ============================




a = int(input("Enter any value between 5 and 9")) 
if(a<5  or a>9): 
  raise  ValueError("Value should be between 5 and 9") 