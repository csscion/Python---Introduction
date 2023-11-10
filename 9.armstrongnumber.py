
num = int(input("Enter a number: "))

num_str = str(num)
print("Number of digits:", len(num_str))

sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   #finds remainder after dividing by 10 and stores in digit
   sum += digit ** len(num_str)

   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")