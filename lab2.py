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


#Operators:
print(10 + 5)

"""
Python divides the operators in the following groups:

  — Arithmetic operators
  — Assignment operators
  — Comparison operators
  — Logical operators
  — Identity operators
  — Membership operators
  — Bitwise operators
"""
"""
+ 	Addition	
- 	Subtraction	
* 	Multiplication	
/ 	Division 	
% 	Modulus	
** 	Exponentiation	
// 	Floor division
"""
"""
Assignment operators are used to assign values to variables:

= 	x = 5 	
+= 	x += 3 	
-= 	x -= 3  	
*= 	x *= 3 	
/= 	x /= 3 	
%= 	x %= 3	
//= 	x //= 3	
**= 	x **= 3	
&= 	x &= 3	
|= 	x |= 3	
^= 	x ^= 3 	
>>= 	x >>= 3
<<= 	x <<= 3
:= 	print(x := 3)
"""

"""
Comparison operators are used to compare two values:

== 	Equal 	
!= 	Not equal
> 	Greater than	
< 	Less than
>= 	Greater than or equal to	
<= 	Less than or equal to
"""

"""
Logical operators are used to combine conditional statements:

and — Returns True if both statements are true
or — Returns True if one of the statements is true
not — Reverse the result, returns False if the result is true
"""

"""
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

is — Returns True if both variables are the same object
is not — Returns True if both variables are not the same object
"""

"""
Membership operators are used to test if a sequence is presented in an object:

in — Returns True if a sequence with the specified value is present in the object	
not in — Returns True if a sequence with the specified value is not present in the object
"""

"""

&  	AND 	Sets each bit to 1 if both bits are 1	
| 	OR 	Sets each bit to 1 if one of two bits is 1
^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
~ 	NOT 	Inverts all the bits
<< 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""

#Operator Precedence:

#Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3)) 

#Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(100 + 5 * 3)

"""
Precedence from top to bottom:

()  —  Parentheses 	
**  —  Exponentiation 	
+x  -x  ~x  —  Unary plus, unary minus, and bitwise NOT 	
*  /  //  %  —  Multiplication, division, floor division, and modulus 	
+  -  —  Addition and subtraction 	
<<  >>  —  Bitwise left and right shifts 	
&  —  Bitwise AND 	
^  —  Bitwise XOR 	
|  —  Bitwise OR 	
==  !=  >  >=  <  <=  is  is not  in  not in  —  Comparisons, identity, and membership operators 	
not  —  Logical NOT 	
and  —  AND 	
or  —  OR
"""

#If two or more operators have the same precedence, the expression is evaluated from left to right.
print(5 + 4 - 7 + 3)


#Lists:
#Lists are created using square brackets []:
thislist = ["apple", "banana", "cherry"]
print(thislist)

"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
"""
#Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#Length of list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#Lists can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#And allow to contain different data types:
list1 = ["abc", 34, True, 40, "male"]

#data type - 'list'
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#List constructor:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Indexes: (starts from 0)
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#Negative indexing means start from the end (-1 last item, -2 second last item)
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of Indexes:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])


#Check if Item Exists:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change Item Value:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change a Range of Item Values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#if more elements than the range are being replaced: 
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#if less elements than the range are being replaced:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#insert - inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append - adds new item to the end:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#extend - adds items from another list to the current to the end:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#allows to append not only list, but any iterable objects (tuple, set, dictionary):
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove - removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#if there is more than 1 items, removes the first occurence;
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#pop - removes the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#if there is no specific index, the pop() method removes the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#del - removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#and can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist

#clear - emtpies the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List.
#for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) 

#Loop Through the Index Numbers.
#range() and len():
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#while loop:
thislist = ["apple", "banana", "cherry"]
index = 0
while(index < len(thislist)):
  print(thislist[index])
  index += 1

#Looping Using List Comprehension:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list comprehension:
#instead of this:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

#we can write this:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#The Syntax
#newlist = [expression for item in iterable if condition == True]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits] 
print(newlist)
#iterable:
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5] 
print(newlist)
newlist = [x.upper() for x in fruits] 
print(newlist)
newlist = ['hello' for x in fruits] 
print(newlist)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#sorting lists.
#sort(): (alphanumerically)
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] #alphabetically
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23] #numerically
thislist.sort()
print(thislist)

#Sort Descending:
#reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] 
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Customize Sort Function.
#key = function:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#the sort() method is case sensitive:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#uppercase letters first and then lowercase

#str.lower - change priority
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order.
#reverse():
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy lists.
#We cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2
#copy():
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#list():
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#slice operator ":" :
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#join two lists:
# + operator:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3) 
#append:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1) 
#extend:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) 

#List methods:
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""

#Tuples.
#A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets ().
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#len():
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#to create a tuple with one item, it should have a comma after the item
thistuple = ("apple",) #tuple
print(type(thistuple))
#NOT a tuple
thistuple = ("apple") #str
print(type(thistuple))

#Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)\

#A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")
#type - 'tuple'
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#tuple():
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#indexing is the same as in lists!!!

#Change Tuple Values:
#convert into a list method:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) 
#Add Items.
#convert into a list method:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#add tuple to tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#Remove items.
#convert into a list method:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#del - delete a tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) this will raise an error because the tuple no longer exists 

#Unpacking a Tuple.
#packing a tuple:
fruits = ("apple", "banana", "cherry")
#But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#The number of variables must match the number of values in the tuple, if not, it must use an asterisk to collect the remaining values as a list.

#Asterisk*:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#----
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#Loop tuples the same as in lists!!!

#Join tuples the same as in lists!!!
#Note: new — multiplication of lists/tuples etc.

#Tuple methods: (only two)
"""
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
"""