#Boolean - True or False
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The bool() function allows to evaluate any value, and give True or False in return
print(bool("Hello")) #True
print(bool(15)) #True

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""
Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

bool("abc") #True
bool(123) #True
bool(["apple", "cherry", "banana"]) #True

#False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#Object that is made from a class with a __len__ function that returns 0 or False evaluates to False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

#Functions can Return a Boolean
def myFunction() :
  return True

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Also built-in functions can return boolean value:
x = 200
print(isinstance(x, int))