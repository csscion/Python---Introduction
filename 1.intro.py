a="Suraj "  
b= 2304  
c= 54.34  
d= complex(5,6)  
e= True  
f= None  
g= ("Suraj" , 123, [1, "sur"])  
h= [1,2.3,"suraj",("S","T","D"),[5,6]]  
i= {"name":"suraj","surname":"damgude"}  
#type(variable_name) is used to determine data type 
print("Type of a is",type(a) )  
print("Type of b is",type(b))  
print("Type of c is",type(c))  
print("Type of d is",type(d))  
print("Type of e is",type(e))  
print("Type of f is",type(f))  
print("sequence ",type(g),g, sep=" - ")  
print("sequence ",type(h),h, sep=" - ")  
print("Dictionary ",type(i),i, sep=" - ")  

# -----------escape sequence-----------------

print("Hello world!" , "Date is", 200123, sep="~~~~", end="0000\n" )  

print("new line",end="\n\n")  

print("\tHello world! \tSuraj here. \nLet's learn Python for \"DATA SCIENCE\"" )  

# raw string(adding r/R before string) ignores all escape sequences and prints them as normal string characters  

print(r"Hello world! \tSuraj here. \nLet's learn Python for \"DATA SCIENCE\"" ,end="\n\n")  

# -----------calculator-----------------

n = 15 
m = 7 
ans1 = n+m 
print("Addition of",n,"and",m,"is", ans1) 
ans2 = n-m 
print("Subtraction of",n,"and",m,"is", ans2) 
ans3 = n*m 
print("Multiplication of",n,"and",m,"is", ans3) 
ans4 = n/m 
print("Division of",n,"and",m,"is", ans4) 
ans5 = n%m 
print("Modulus of",n,"and",m,"is", ans5) 
ans6 = n//m 
print("Floor Division of",n,"and",m,"is", ans6) 
# ----------------------------

