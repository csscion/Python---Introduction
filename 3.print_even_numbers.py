n=int(input("enter the number till which you wish to enlist all even numbers"))

'using for loop'
print('"running for loop')
for i in range (1, n+1):
    if (i%2 ==0):
        print (i)
    else:
        i+=1

'using while loop'
j=1
print('"running while loop')
while (j<=n):
    if (j%2 ==0):
        print(j)
    j+=1

'using break in while loop'
print('using break in while loop')
k=1
while (True):
    if (k>n):
        break
    elif(k%2 ==0):
        print(k)
    k+=1
   
'using continue in while loop'
l=0
print('using continue in while loop')
while(l<=n-1):
    l+=1
    if (l%2!= 0):
        continue
    print(l)