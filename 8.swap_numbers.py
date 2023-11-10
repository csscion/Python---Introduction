
num1 =int(input('enter first number:'))
num2=int(input('enter second number:'))


print("Using temp variable" )
print("before swap", num1,num2 )

temp=num1
num1=num2
num2=temp

print("after swap", num1,num2 )

# '-----------------------------------------'
# '-----------------------------------------'

print("withot using temp variable" )
print("before swap", num1,num2 )
num1 = num1 + num2 
num2 = num1 - num2
num1 = num1 - num2
print("after swap", num1,num2 )

