import random
import math

print(dir(math))
elements = [1,2,3,4,5,6,7,8,9,10]
print(random.choice(elements))

print(random.randrange(20,50,3))

print(random.random())

print(random.random())
print("========================")
random.seed(1)
print(random.random())
print(random.random())
print("========================")
random.seed(2)
print(random.random())
print(random.random())
print("========================")
random.seed(1)
print(random.random())
print(random.random())
print("========================")
random.seed(2)
print(random.random())
print(random.random())
print("========================")
random.seed(3)
print(random.random())
print(random.random())
print("========================")